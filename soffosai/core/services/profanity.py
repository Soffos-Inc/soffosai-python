'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-27
Purpose: Easily use Profanity Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class ProfanityService(SoffosAIService):
    '''
    This module detects profanities and the level of offensiveness in a body of text.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.PROFANITY
        super().__init__(service, **kwargs)
    

    def __call__(self, user:str, text:str):
        self._args_dict = inspect_arguments(self.__call__, user, text)
        return super().__call__()
