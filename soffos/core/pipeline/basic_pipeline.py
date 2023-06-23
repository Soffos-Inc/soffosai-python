'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-21
Purpose: Define the basic pipeline object
-----------------------------------------------------
'''
import soffos
from soffos.core.nodes.node import NodeConfig


class SoffosPipeline:
    def __init__(self, stages:list, use_defaults:bool=True, **kwargs) -> None:
        self._apikey = kwargs['apikey'] if kwargs.get('apikey') else soffos.api_key
        self._stages = stages
        self._input:dict = {}
        self._infos = []

        for stage in stages:
            stage:NodeConfig

        error_messages = []
        if not isinstance(stages, list):
            error_messages.append("stages field should be a list of Service Nodes")
        for stage in stages:
            if not isinstance(stage, NodeConfig):
                error_messages.append(f"{stage} is not an instance of NodeConfig")
        
        if len(error_messages) != 0:
            raise ValueError(error_messages)
        
        if "text" in self._source.keys():
            self._source["document_text"] = self._source["text"]
        
        self._outputfields = [stage.service._serviceio.output_structure.keys() for stage in self._stages]
        self.validate_pipeline()


    def validate_pipeline(self):
        error_messages = []
        #  Get output keys as reference for Node's input keys
        

        #  The first available keys are of the source
        self._outputfields.insert(0, self._source.keys())

        for i, stage in enumerate(self._stages):
            # check if the node/stage has complete source keys
            node_is_valid, err = stage.service.allow_input()
            if not node_is_valid:
                error_messages.append(err)

            # Check if the source keys specified on the Node can be captured from the source or output of ther Nodes
            stage:NodeConfig
            if i == 0:
                for key,value in stage.source.items():
                    if isinstance(value, tuple):
                        reference_node_number = value[0]
                        required_key = value[1]
                        if reference_node_number > 0:
                            raise ValueError("The first Node cannot reference an output of later Nodes")
                        elif required_key not in self._source.keys():
                            raise ValueError(f"{value[1]} cannot be found in the Pipeline's source")

            else:
                for key, value in stage.source.items():
                    if isinstance(value, tuple):
                        reference_node_number = value[0]
                        required_key = value[1]
                        if reference_node_number > i:
                            raise ValueError("Cannot reference the output as input of later or current Node")
                        if required_key not in self._outputfields[reference_node_number]:
                            _note = f"output of Node {reference_node_number}" if reference_node_number > 0 else "source"
                            error_messages.append(f"cannot map {required_key} in the {_note}.")

        if len(error_messages) != 0:
            raise ValueError(error_messages)
        
        return True


    def run(self) -> dict:
        
        for i, node in enumerate(self._stages):
            node:ServiceNode
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
                src['user'] = self._user

            response:dict = node.run(source = src)
            print(f"response ready for {node.service._service}")
            # update outputfields values
            self._infos.append(response)

        return self._infos

    def add_node(self, node:ServiceNode):
        self._stages.append(node)
