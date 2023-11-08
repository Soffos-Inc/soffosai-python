'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-11-08
Purpose: Easily use Chat Bots Get Service
-----------------------------------------------------
'''
from .service import SoffosAIService
from .input_config import InputConfig
from soffosai.common.constants import ServiceString
from typing import Union



class ChatBotsGetService(SoffosAIService):
    '''
    This endpoint allows you to get the information of previously created chatbots.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.CHAT_BOTS_GET
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, chatbot_ids:list=None) -> dict:
        '''
        Call the Chat Bots Get Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param chatbot_ids: Specify the id of the chatbots you need to see the details for. Don't pass
            this parameter if you wish to see all your created chatbots.
        :return: chatbots: A list of dictionaries with details about your chatbots.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bots_get.py>`_
        '''
        return super().__call__(user=user, chatbot_ids=chatbot_ids)

    def set_input_configs(self, name:str, chatbot_ids:Union[list, InputConfig]=None):
        super().set_input_configs(name=name, chatbot_ids=chatbot_ids)

    @classmethod
    def call(self, user:str, chatbot_ids:list=None) -> dict:
        '''
        Call the Chat Bots Get Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param chatbot_ids: Specify the id of the chatbots you need to see the details for. Don't pass
            this parameter if you wish to see all your created chatbots.
        :return: chatbots: A list of dictionaries with details about your chatbots.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bots_get.py>`_
        '''
        return super().call(user=user, chatbot_ids=chatbot_ids)

