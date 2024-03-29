'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2024-03-03
Purpose: Easily use Paraphrase Service
-----------------------------------------------------
'''
from .service import SoffosAIService
from .input_config import InputConfig
from soffosai.common.constants import ServiceString
from typing import Union


class ParaphraseService(SoffosAIService):
    '''
    Paraphrase and Simplify are available as two different flavors of the same
    module. While the Paraphrase module attempts to change the wording while
    keeping the same level of complexity, the Simplify module outputs more commonly
    used words without altering the meaning of the original text.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.PARAPHRASE
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str, engine:str=None) -> dict:
        '''
        Call the Paraphrase Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param text: Text to be paraphrased/simplified.
        :param engine: The LLM engine to be used.
        :return: engine: The LLM engine used.
        paraphrase: The paraphrased text.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/paraphrase.py>`_
        '''
        return super().__call__(user=user, text=text, engine=engine)

    def set_input_configs(self, name:str, text:Union[str, InputConfig], engine:Union[str, InputConfig]=None):
        super().set_input_configs(name=name, text=text, engine=engine)

    @classmethod
    def call(self, user:str, text:str, engine:str=None) -> dict:
        '''
        Call the Paraphrase Service
        
        :param user: The ID of the user accessing the Soffos API.
            This string will be used for throttling and profanity tracking.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        :param text: Text to be paraphrased/simplified.
        :param engine: The LLM engine to be used.
        :return: engine: The LLM engine used.
        paraphrase: The paraphrased text.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/paraphrase.py>`_
        '''
        return super().call(user=user, text=text, engine=engine)

