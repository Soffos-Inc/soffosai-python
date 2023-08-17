'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-17
Purpose: Soffos Service base Node
-----------------------------------------------------
'''
from typing import Union
from soffosai.common.serviceio_fields import ServiceIO
from soffosai.core.services import SoffosAIService
from soffosai.common.constants import ServiceString


class Node:
    '''
    A SoffosAIService wrapper that holds information how the service is to be executed inside a 
    SoffosPipeline
    '''
    _service_io: ServiceIO

    def __init__(self, name, service:Union[ServiceString, SoffosAIService], source:dict={}) -> None:
        
        self._raw_service = service
        self.name = name
        self.source_config = source
        if isinstance(service, str):
            self.service:SoffosAIService = SoffosAIService(service=service)
        elif issubclass(service, SoffosAIService):
            self.service:SoffosAIService = service()
        else:
            raise ValueError("Upon initialization of the Node: invalid argument value for <service>.")
        

    def validate_node(self):
        '''
        Will check if the Node will run from the given source. Will also create the proper 
        source for the SoffosAIService
        '''
        validated_data = {}
        for key,value in self.source_config.items():
            if not isinstance(value, tuple):
                validated_data[key] = value
            else:
                raise ValueError(f"This source notation is only valid in a Pipeline. To execute a single node, provide the actual value for each source key")
            
        return validated_data


    def run(self, payload=None):
        if payload is not None:
            self.source_config = payload
            
        args = self.validate_node()

        return self.service.get_response(payload=payload)

    
    def __call__(self, payload={}, *args, **kwargs):
        '''
        This feature is only for testing/debugging a Node.
        To easily create and call a service, please use the SoffosAIService class
        '''
        self.service.get_response(payload=payload, *args, **kwargs)
