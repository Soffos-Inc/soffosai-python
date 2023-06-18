'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-17
Purpose: Soffos Service base Node
-----------------------------------------------------
'''
from soffos.common.serviceio_fields import ServiceIO
from soffos.core.services import SoffosAIService

class ServiceNode:
    _service_io: ServiceIO

    def __init__(self, service:SoffosAIService, source=None) -> None:
        self.source = source
        self.service:SoffosAIService = service
        if source is not None:
            self.validate()


    def validate(self):
        '''
        Will check if the Node will run from the given source. Will also create the proper 
        source for the SoffosAIService
        '''
        self.validated_data = {}
        for key,value in self.source.items():
            if not isinstance(value, tuple):
                self.validated_data[key] = value
            elif value[0] == 0:
                self.validated_data[key] = value[1]
            else:
                raise ValueError(f"This is a single node, cannot reference {value[0]}th node")
        
        return self.validated_data


    def run(self, source=None):
        if source is not None:
            self.source = source
            self.validate()
        try:
            args = self.validated_data
        except AttributeError as e:
            raise AttributeError("Please provide a source either in the constructor or in the run arguments") from e

        user = args.pop('user')
        service = self.service(user=user, src=args)
        return service.get_response()
