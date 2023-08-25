'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-08-14
Purpose: Define the basic pipeline object
-----------------------------------------------------
'''
import soffosai
from soffosai.core.nodes.node import Node


def is_node_input(value):
    if not isinstance(value, dict):
        return False
    return "source" in value and "field" in value


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
    def __init__(self, nodes:list, use_defaults:bool=False, **kwargs) -> None:
        self._apikey = kwargs['apikey'] if kwargs.get('apikey') else soffosai.api_key
        self._stages = nodes
        self._input:dict = {}
        self._infos = []
        self._use_defaults = use_defaults
        self._execution_codes = []
        self._termination_codes = []

        error_messages = []
        if not isinstance(nodes, list):
            error_messages.append('stages field should be a list of Service Nodes')

        for node in nodes:
            if not isinstance(node, Node):
                error_messages.append(f'{node} is not an instance of Node.')

        if len(error_messages) > 0:
            raise ValueError("\\n".join(error_messages))

        self._outputfields = [list(stage.service._serviceio.output_structure.keys()) for stage in self._stages]

    
    def run(self, user_input):
        if not isinstance(user_input, dict):
            raise ValueError("User input should be a dictionary.")

        if "user" not in user_input:
            raise ReferenceError("'user' is not defined in the user_input.")

        if "text" in user_input:
            user_input['document_text'] = user_input['text']
        
        if self._use_defaults:
            stages = self.set_defaults(self._stages, user_input)
        else:
            stages = self._stages

        # termination referencing
        execution_code = user_input.get("execution_code")
        if execution_code:
            execution_code = self._apikey + execution_code
            if execution_code in self._execution_codes:
                raise ValueError("This execution code is still being used in an existing pipeline run.")
            else:
                self._execution_codes.append(execution_code)

        self.validate_pipeline(user_input, stages)

        # Initialization of values
        infos = {}
        infos['user_input'] = user_input
        total_cost = 0.00

        # Execute per stage
        for stage in stages:
            stage: Node
            # premature termination
            if execution_code in self._termination_codes:
                self._termination_codes.remove(execution_code)
                self._execution_codes.remove(execution_code)
                infos['total_cost'] = total_cost
                infos['wargning'] = "This Soffos Pipeline has been prematurely terminated"
                return infos
            
            # execute
            print(f"running {stage.service._service}.")
            tmp_source: dict = stage.source
            payload = {}
            for key, notation in tmp_source.items():
                # prepare payload
                if is_node_input(notation): # value is pointing to another node
                    value = infos[notation['source']][notation['field']]
                    if "pre_process" in notation:
                        if callable(infos[notation['pre_process']]):
                            payload[key] = notation['pre_process'](value)
                        else:
                            raise ValueError(f"{stage.name}: pre_process value should be a function.")
                    
                    else:
                        payload[key] = value
                else:
                    payload[key] = notation

            if 'user' not in payload:
                payload["user"] = user_input['user']
            
            payload['apikey'] = self._apikey

            response = stage.service.get_response(payload)
            if "error" in response:
                raise ValueError(response)
            
            print(f"Response ready for {stage.name}")
            infos[stage.name] = response
            total_cost += response['cost']['total_cost']

        infos['total_cost'] = total_cost

        # remove this execution code from execution codes in effect:
        if execution_code:
            self._execution_codes.remove(execution_code)

        return infos


    def validate_pipeline(self, user_input, stages):
        '''
        Before running the first service, the Pipeline will validate all nodes if they will all be
        executed successfully with the exception of database and server issues.
        '''
        error_messages = []
        self._outputfields.insert(0, user_input.keys())

        for stage in stages:
            stage: Node
            serviceio = stage.service._serviceio
            # checking required_input_fields is already handled in the Node's constructor

            # check if require_one_of_choices is present and not more than one
            if len(serviceio.require_one_of_choice) > 0:
                group_errors = []
                for group in serviceio.require_one_of_choice:
                    found_choices = [choice for choice in group if choice in stage.source]
                    if not found_choices:
                        group_errors.append(f"{stage.name}: Please provide one of these values on your payload: {group}.")
                    elif len(found_choices) > 1:
                        group_errors.append(f"Please include only one of these values: {group}.")
                    
                if len(group_errors) > 0:
                    error_messages.append(". ".join(group_errors))
            
            # check if datatypes are correct:
            for key, notation in stage.source.items():
                try:
                    required_datatype = self.get_serviceio_datatype(stage.service._serviceio.input_structure[key])
                except KeyError:
                    continue
                
                if is_node_input(notation):
                    if "pre_process" in notation:
                        continue # will not check for type if there is a helper function
                    
                    if notation['source'] == "user_input":
                        user_input_type = type(user_input[notation['field']])
                        if user_input_type != required_datatype:
                            error_messages.append(f"{stage.name}: {required_datatype} required on user_input '{key}' field but {user_input_type} is provided.")
                    else:
                        for subnode in stages:
                            subnode: Node
                            if notation['source'] == subnode.name:
                                output_datatype = self.get_serviceio_datatype(subnode.service._serviceio.output_structure[notation['field']])
                                if output_datatype != required_datatype:
                                    error_messages.append(f"On {stage.name} node: The input datatype required for field ${key} is {required_datatype}. This does not match the datatype to be given by node ${subnode.name}'s ${notation['field']} field which is ${output_datatype}.")
                            break
                
                else:
                    if type(notation) != required_datatype:
                        error_messages.append(f"On {stage.name} node: {key} requires ${required_datatype} but ${type(notation)} is provided.")

        if len(error_messages) > 0:
            raise ValueError(error_messages)
        
        return True


    def add_node(self, node):
        if isinstance(node, Node):
            self._stages.append(node)
        else:
            raise ValueError(f"{node} is not a Node instance")

    
    def set_defaults(self, stages, user_input):
        defaulted_stages = []
        for i, stage in enumerate(stages):
            stage: Node
            stage_source = {}
            required_keys = stage.service._serviceio.required_input_fields
            require_one_choices = stage.service._serviceio.require_one_of_choice
            if len(require_one_choices) > 0:
                for choices in require_one_choices:
                    required_keys.append(choices[0]) # the default argument is the first one
            
            for required_key in required_keys:
                check_key = stage.source.get(required_key)
                if check_key and check_key != "default":
                    stage_source[required_key] = check_key
                    continue

                found_input = False
                for j in range(i-1, -1, -1):
                    stage_for_output:Node = stages[j]
                    stage_for_output_output_fields = stage_for_output.service._serviceio.output_structure
                    if required_key in stage_for_output_output_fields:
                        stage_source[required_key] = {
                            "source": stage_for_output.name,
                            "field": required_key
                        }
                        found_input = True
                
                    # special considerations:
                    elif required_key == "context" and "text" in stage_for_output_output_fields:
                        stage_source["context"] = {
                            "source": stage_for_output.name,
                            "field": "text"
                        }
                        found_input = True

                    elif required_key == "document_text" and "text" in stage_for_output_output_fields:
                        stage_source["document_text"] = {
                            "source": stage_for_output.name,
                            "field": "text"
                        }
                        found_input = True
                    
                if not found_input:
                    if required_key in user_input:
                        stage_source[required_key] = user_input[required_key]
                        stage_source[required_key] = {
                            "source": "user_input",
                            "field": required_key
                        }
                    else:
                        raise ReferenceError(f"Please add {required_key} to user input. The previous Nodes' outputs do not provide this data.")

            defaulted_stage = Node(stage.name, stage.service, stage_source)
            defaulted_stages.append(defaulted_stage)
        
        return defaulted_stages

    
    def terminate(self, termination_code):
        if termination_code:
            self._termination_codes.append(self._apikey + termination_code)
            return {"message": f"Request to terminate job {termination_code} received."}

        return {"message": f"Request to terminate job is not valid (execution code missing)."}


    def get_serviceio_datatype(self, key):
        if isinstance(key, type):
            return key
        return type(key)
    
    def __call__(self, user_input):
        return self.run(user_input)