'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2024-03-03
Purpose: Easily use Discuss Query Service
-----------------------------------------------------
'''
from .service import SoffosAIService
from .input_config import InputConfig
from soffosai.common.constants import ServiceString
from typing import Union


class DiscussQueryService(SoffosAIService):
    '''
    The Let's Discuss module allows the user to have a conversation with the AI
    about the content provided by the user. The main difference between this module
    and the Question Answering module is that Let's Discuss keeps a history of the
    interactions, allowing it to take in account what was previously discussed when
    generating a response. Unlike Question Answering which is mainly used for
    information retrieval, the Let's Discuss module creates a more natural
    experience similar to having a conversation with a person at the expense of the
    size of the content it can process at a time.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.DISCUSS_QUERY
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, query:str, session_id:str, engine:str=None) -> dict:
        '''
        Call the Discuss Query Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param query: User's message.
        :param engine: The LLM engine to be used.
        :return: engine: The LLM engine used.
        response: Module's response to the user's query.
        context: The context discussed about provided by the user during session
            creation.
        messages: A list of dictionaries representing all the messages exchanged
            between the user and the system for the specific session. The
            messages are sorted in chronological order. Each dictionary
            contains the following fields: text: The message. source: The
            source of the message, which is either the user or Soffos.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/discuss_query.py>`_
        '''
        return super().__call__(user=user, query=query, session_id=session_id, engine=engine)

    def set_input_configs(self, name:str, query:Union[str, InputConfig], engine:Union[str, InputConfig]=None):
        super().set_input_configs(name=name, query=query, engine=engine)

    @classmethod
    def call(self, user:str, query:str, session_id:str, engine:str=None) -> dict:
        '''
        Call the Discuss Query Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param query: User's message.
        :param engine: The LLM engine to be used.
        :return: engine: The LLM engine used.
        response: Module's response to the user's query.
        context: The context discussed about provided by the user during session
            creation.
        messages: A list of dictionaries representing all the messages exchanged
            between the user and the system for the specific session. The
            messages are sorted in chronological order. Each dictionary
            contains the following fields: text: The message. source: The
            source of the message, which is either the user or Soffos.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/discuss_query.py>`_
        '''
        return super().call(user=user, query=query, session_id=session_id, engine=engine)

