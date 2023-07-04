'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-21
Purpose: Define the basic pipeline object
-----------------------------------------------------
'''
import soffosai
from soffosai.core.nodes_configs.node import NodeConfig


class Pipeline:
    '''
    A controller for consuming multiple Services called stages.
    It validates all inputs of all stages before sending the first Soffos API request to ensure
    that the Pipeline will not waste credits.
    
    ** use_defaults=True means that stages will take input from the previous stages' 
    output of the same field name prioritizing the latest stage's output. 
    If the previous stages does not have it, it will take from the
    pipeline's user_input.  Also, the stages will only be supplied with the required fields + default
    of the require_one_of_choice fields.
    '''
    def __init__(self, stages:list, use_defaults:bool=False, **kwargs) -> None:
        self._apikey = kwargs['apikey'] if kwargs.get('apikey') else soffosai.api_key
        self._stages = stages
        self._input:dict = {}
        self._infos = []

        error_messages = []
        if not isinstance(stages, list):
            error_messages.append("stages field should be a list of Service Nodes")
        for stage in stages:
            if not isinstance(stage, NodeConfig):
                error_messages.append(f"{stage} is not an instance of NodeConfig")

        if len(error_messages) != 0:
            raise ValueError(error_messages)
        
        self._outputfields = [stage.service._serviceio.output_structure.keys() for stage in self._stages]
        
        if use_defaults:
            self._stages = self.set_defaults(self._stages)


    def validate_pipeline(self):
        '''
        Before running the first service, the Pipeline will validate all nodes if they will all be
        executed successfully with the exception of database and server issues.
        '''
        error_messages = []

        #  The first available keys are of the source
        self._outputfields.insert(0, self._input.keys())

        for i, stage in enumerate(self._stages):
            
            stage.service._payload = {}
            # Check if the source keys specified on the Node can be captured from the source or output of other Nodes
            stage:NodeConfig
            if i == 0:
                for key,value in stage.source.items():
                    if isinstance(value, tuple):
                        reference_node_number = value[0]
                        required_key = value[1]
                        if reference_node_number > 0:
                            error_messages.append("The first Node cannot reference an output of later Nodes")
                        elif required_key not in self._input.keys():
                            error_messages.append(f"{value[1]} cannot be found in the Pipeline's source")
                        
                        # correction for document_id and document_ids
                        if key == "document_ids" and required_key == "document_id":
                            stage.service._payload[key] = [self._input[required_key]]
                        else:
                            # update the temporary payload for service validation
                            stage.service._payload[key] = self._input[required_key]
                    
                    else:
                        stage.service._payload[key] = value

            else:
                for key, value in stage.source.items():
                    if isinstance(value, tuple):
                        reference_node_number = value[0]
                        required_key = value[1]
                        if reference_node_number > i: # value[0] refers to the output of the node, i refers to the node itself, different index 
                            error_messages.append(f"stage {i+1}. {stage.service._service}: Cannot reference the output of later or current Node")
                        if required_key not in self._outputfields[reference_node_number]:
                            _note = f"output of Node {reference_node_number}" if reference_node_number > 0 else "source"
                            error_messages.append(f"cannot map {required_key} in the {_note}.")
                        
                        # update the temporary payload for service validation
                        if reference_node_number == 0: # get from source
                            stage.service._payload[key] = self._input[required_key]
                            
                        else: # get from  other node/stage. 
                            ref_node = reference_node_number - 1 # because you are refencing a node, not node output
                            try:
                                # get the type from serviceio but also consider document_ids when given document_id
                                required_type = self._stages[ref_node].service._serviceio.output_structure[required_key]
                                stage.service._payload[key] = required_type if key != "document_ids" else [required_type]
                            except KeyError:
                                error_messages.append(f"stage{i+1}:{required_key} is not available in {self._stages[ref_node].service._service} output")
                    else:
                        stage.service._payload[key] = value

            # check if the node/stage has complete source keys and correct type
            if "document_id" in stage.service._payload.keys():
                if "document_ids" in stage.service._payload.keys():
                    stage.service._payload['document_ids'].append(stage.service._payload["document_id"])
                else:
                    stage.service._payload['document_ids'] = [stage.service._payload["document_id"]]

            if 'user' not in stage.service._payload.keys():
                stage.service._payload['user'] = self._input.get('user')

            node_is_valid, err = stage.service.validate_payload()
            if not node_is_valid:
                error_messages.append(err)

        if len(error_messages) != 0:
            raise ValueError(error_messages)
        
        return True


    def run(self, user_input:dict) -> dict:
        self._input = user_input
        
        if "text" in self._input.keys():
            self._input["document_text"] = self._input["text"]

        self.validate_pipeline()
        self._infos.append(user_input)

        for i, node in enumerate(self._stages):
            node:NodeConfig
            print(f"running {node.service._service}")
            temp_src = node.source
            src = {}
            
            for key, value in temp_src.items():
                if isinstance(value, tuple):
                    set_value = self._infos[value[0]][value[1]]
                else:
                    set_value = value
                
                if key == "document_ids" and value[1] == "document_id":
                    set_value = [set_value]

                src[key] = set_value
            
            if not src.get('user'):
                src['user'] = user_input.get('user')

            response:dict = node.service.get_response(payload = src)
            if 'error' in response:
                raise ValueError(response)
            print(f"response ready for {node.service._service}")
            # update outputfields values
            self._infos.append(response)

        return self._infos

    def add_node(self, node:NodeConfig):
        self._stages.append(node)


    def __call__(self, user_input):
        return self.run(user_input)


    def set_defaults(self, stages):
        defaulted_stages = []
        for i, stage in enumerate(stages):
            # initialize the acquired source
            stage_source = {}
            # Take the required inputs
            required_keys:list = stage.service._serviceio.required_input_fields
            if len(stage.service._serviceio.require_one_of_choice) > 0:
                for group in stage.service._serviceio.require_one_of_choice:
                    required_keys.append(group[0])

            for key in required_keys:
                # check the output of previous stage
                if i > 0:
                    found_key = False
                    for j in range(i):
                        previous_output_fields = self._stages[j].service._serviceio.output_structure.keys()
                        if key in previous_output_fields:
                            stage_source[key] = (j+1, key)
                            found_key = True

                    if not found_key:
                        # if not found, set it to the user_input
                        stage_source[key] = (0, key)
                
                else:
                    stage_source[key] = (0, key)

            defaulted_stage = NodeConfig(service=stage.service, source=stage_source)
            defaulted_stages.append(defaulted_stage)
            print(defaulted_stages)
        
        return defaulted_stages
