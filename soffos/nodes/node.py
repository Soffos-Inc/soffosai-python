'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-17
Purpose: Soffos Service base Node
-----------------------------------------------------
'''
from soffos.common.serviceio_fields import ServiceIO
from soffos.core.services import SoffosAIService
from soffos.common.constants import ServiceString


class ServiceNode:
    '''
    A SoffosAIService wrapper that holds information how the service is to be executed inside a 
    SoffosPipeline
    '''
    _service_io: ServiceIO

    def __init__(self, service:ServiceString, user:str=None, source:dict=None) -> None:
        self.source = source
        self.service:SoffosAIService = SoffosAIService(service=service, src=source, user=user)
        self._user = user


    def validate(self):
        '''
        Will check if the Node will run from the given source. Will also create the proper 
        source for the SoffosAIService
        '''
        validated_data = {}
        for key,value in self.source.items():
            if not isinstance(value, tuple):
                validated_data[key] = value
            else:
                raise ValueError(f"This source notation is only valid in a Pipeline. \
                    To execute a single node, provide the actual value for each source key")
            
            if 'user' not in validated_data.keys() and self._user:
                validated_data['user'] = self._user
            
            if not validated_data.get('user'):
                raise TypeError("user is a required parameter. Provide it as a constructor argument or source item")
        
        return validated_data


    def run(self, source=None):
        if source is not None:
            self.source = source
            
        args = self.validate()

        return self.service.get_response(src=args)
