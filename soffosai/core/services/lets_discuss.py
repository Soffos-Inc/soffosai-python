'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use Let's Discuss Service
-----------------------------------------------------
'''
from typing import Union, Dict
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString
from soffosai.common.service_io_map import SERVICE_IO_MAP
from soffosai.common.serviceio_fields import ServiceIO


class LetsDiscussService(SoffosAIService):
    '''
    The Let's Discuss module allows the user to have a conversation with the AI about the content 
    provided by the user. The main difference between this module and the Question Answering module 
    is that Let's Discuss keeps a history of the interactions.
    '''
    def __init__(self,  **kwargs) -> None:
        service = ServiceString.LETS_DISCUSS
        super().__init__(service, **kwargs)


    def create(self, user:str, context:str):
        self._service = ServiceString.LETS_DISCUSS_CREATE
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.create, user, context)
        return self.get_response(payload=self._args_dict)
    

    def __call__(self, user:str, session_id:str, query:str):
        self._service = ServiceString.LETS_DISCUSS
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.__call__, user, session_id, query)
        return super().__call__()
    

    def retrieve_sessions(self, user:str, return_messages:bool):
        self._service = ServiceString.LETS_DISCUSS_RETRIEVE
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.retrieve_sessions, user, return_messages)
        return self.get_response(payload=self._args_dict)
    
    
    def delete(self, user:str, session_ids:list):
        self._service = ServiceString.LETS_DISCUSS_DELETE
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.delete, user, session_ids)
        return self.get_response(payload=self._args_dict)

    
    def set_pipeline_input(self, ref_name:str, session_id:Union[str, Dict], query:Union[str, Dict]) -> None:
        self.source_config = inspect_arguments(self.set_pipeline_input, ref_name, session_id, query)
        return super().set_pipeline_input()


class LetsDiscussCreateService(SoffosAIService):
    '''
    A separate class for LetsDiscuss service to be used for creating a session only.
    '''
    def __init__(self,  **kwargs) -> None:
        service = ServiceString.LETS_DISCUSS_CREATE
        super().__init__(service, **kwargs)


    def __call__(self, user:str, context:str):
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.__call__, user, context)
        return super().__call__()


    def set_pipeline_input(self, ref_name:str, context:Union[str, Dict]) -> None:
        self.source_config = inspect_arguments(self.set_pipeline_input, ref_name, context)
        return super().set_pipeline_input()


class LetsDiscussRetrieveService(SoffosAIService):
    '''
    A separate class for LetsDiscuss service to be used for retrieving sessions only.
    '''
    def __init__(self,  **kwargs) -> None:
        service = ServiceString.LETS_DISCUSS_RETRIEVE
        super().__init__(service, **kwargs)


    def __call__(self, user:str, return_messages:bool):
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.__call__, user, return_messages)
        return super().__call__()
    

    def set_pipeline_input(self, ref_name:str, return_messages:Union[bool, Dict]) -> None:
        self.source_config = inspect_arguments(self.set_pipeline_input, ref_name, return_messages)
        return super().set_pipeline_input()


class LetsDiscussDeleteService(SoffosAIService):
    '''
    A separate class for LetsDiscuss service to be used for deleting sessions only.
    '''
    def __init__(self,  **kwargs) -> None:
        service = ServiceString.LETS_DISCUSS_DELETE
        super().__init__(service, **kwargs)


    def __call__(self, user:str, session_ids:list):
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.__call__, user, session_ids)
        return super().__call__()


    def set_pipeline_input(self, ref_name:str, session_ids:Union[list, Dict]) -> None:
        self.source_config = inspect_arguments(self.set_pipeline_input, ref_name, session_ids)
        return super().set_pipeline_input()
