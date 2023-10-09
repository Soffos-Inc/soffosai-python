'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-10-09
Purpose: Easily use Chat Bot Delete User Sessions Service
-----------------------------------------------------
'''
from .service import SoffosAIService
from .input_config import InputConfig
from soffosai.common.constants import ServiceString
from typing import Union



class ChatBotDeleteUserSessionsService(SoffosAIService):
    '''
    Delete user sessions
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.CHAT_BOT_DELETE_USER_SESSIONS
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, chatbot_id:str, user_id:str, session_ids:list=None) -> dict:
        '''
        Call the Chat Bot Delete User Sessions Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param chatbot_id: Missing Documentation
        :param user_id: Missing Documentation
        :param session_ids: List of the ids of the user sessions to be deleted.
        :return: success: Missing Documentation
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bot_delete_user_sessions.py>`_
        '''
        return super().__call__(user=user, chatbot_id=chatbot_id, user_id=user_id, session_ids=session_ids)

    def set_input_configs(self, name:str, chatbot_id:Union[str, InputConfig], user_id:Union[str, InputConfig], session_ids:Union[list, InputConfig]=None):
        super().set_input_configs(name=name, chatbot_id=chatbot_id, user_id=user_id, session_ids=session_ids)

    @classmethod
    def call(self, user:str, chatbot_id:str, user_id:str, session_ids:list=None) -> dict:
        '''
        Call the Chat Bot Delete User Sessions Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param chatbot_id: Missing Documentation
        :param user_id: Missing Documentation
        :param session_ids: List of the ids of the user sessions to be deleted.
        :return: success: Missing Documentation
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/chat_bot_delete_user_sessions.py>`_
        '''
        return super().call(user=user, chatbot_id=chatbot_id, user_id=user_id, session_ids=session_ids)

