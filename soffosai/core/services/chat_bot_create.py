'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-11-08
Purpose: Easily use Chat Bot Create Service
-----------------------------------------------------
'''
from .service import SoffosAIService
from .input_config import InputConfig
from soffosai.common.constants import ServiceString
from typing import Union



class ChatBotCreateService(SoffosAIService):
    '''
    Creates a chatbot and returns its ID. The id will later be used to allow users
    to interact with it.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.CHAT_BOT_CREATE
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, role:str, document_name:str, chatbot_id:str=None) -> dict:
        '''
        Call the Chat Bot Create Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param role: A description of your bot's purpose. You may also describe its tone when
            responding. The system may not be able to follow complex instructions
            specified in this field.
        :param document_name: The name/identity of your chatbot.
        :param chatbot_id: None
        :return: chatbot_id: None
        success: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bot_create.py>`_
        '''
        return super().__call__(user=user, role=role, document_name=document_name, chatbot_id=chatbot_id)

    def set_input_configs(self, name:str, role:Union[str, InputConfig], document_name:Union[str, InputConfig], chatbot_id:Union[str, InputConfig]=None):
        super().set_input_configs(name=name, role=role, document_name=document_name, chatbot_id=chatbot_id)

    @classmethod
    def call(self, user:str, role:str, document_name:str, chatbot_id:str=None) -> dict:
        '''
        Call the Chat Bot Create Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param role: A description of your bot's purpose. You may also describe its tone when
            responding. The system may not be able to follow complex instructions
            specified in this field.
        :param document_name: The name/identity of your chatbot.
        :param chatbot_id: None
        :return: chatbot_id: None
        success: None
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bot_create.py>`_
        '''
        return super().call(user=user, role=role, document_name=document_name, chatbot_id=chatbot_id)

