'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use Let's Discuss Service
-----------------------------------------------------
'''
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


    def create(self, user, context):
        self._service = ServiceString.LETS_DISCUSS_CREATE
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.create, user, context)
        return self.get_response(payload=self._args_dict)
    

    def __call__(self, user, session_id, query):
        self._service = ServiceString.LETS_DISCUSS
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.__call__, user, session_id, query)
        return super().__call__()
    

    def retrieve_sessions(self, user, return_messages:bool):
        self._service = ServiceString.LETS_DISCUSS_RETRIEVE
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.retrieve_sessions, user, return_messages)
        return self.get_response(payload=self._args_dict)
    
    
    def delete(self, user, session_ids:list):
        self._service = ServiceString.LETS_DISCUSS_DELETE
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.delete, user, session_ids)
        return self.get_response(payload=self._args_dict)
