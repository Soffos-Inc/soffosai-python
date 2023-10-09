'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-10-09
Purpose: Easily use Contradiction Detection Service
-----------------------------------------------------
'''
from .service import SoffosAIService
from .input_config import InputConfig
from soffosai.common.constants import ServiceString
from typing import Union



class ContradictionDetectionService(SoffosAIService):
    '''
    This module finds conflicting information in a body of text and returns a
    description of the contradiction along with the relevant sentences and their
    offsets within the original text.
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.CONTRADICTION_DETECTION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str) -> dict:
        '''
        Call the Contradiction Detection Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be analyzed for contradictions. Up to 10000 characters.
        :return: contradictions: A list of dictionaries representing detected contradictions. Each
            dictionary contains the following fields: contradiction: A description of
            the contradiction. sentences: A list of sentences related to the
            contradiction. Each sentence is a dictionary with the sentence's text,
            starting offset and ending offset within the original text.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/contradiction_detection.py>`_
        '''
        return super().__call__(user=user, text=text)

    def set_input_configs(self, name:str, text:Union[str, InputConfig]):
        super().set_input_configs(name=name, text=text)

    @classmethod
    def call(self, user:str, text:str) -> dict:
        '''
        Call the Contradiction Detection Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be analyzed for contradictions. Up to 10000 characters.
        :return: contradictions: A list of dictionaries representing detected contradictions. Each
            dictionary contains the following fields: contradiction: A description of
            the contradiction. sentences: A list of sentences related to the
            contradiction. Each sentence is a dictionary with the sentence's text,
            starting offset and ending offset within the original text.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/contradiction_detection.py>`_
        '''
        return super().call(user=user, text=text)

