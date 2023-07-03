'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use Contradiction Detection Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class ContradictionDetectionService(SoffosAIService):
    '''
    This module finds conflicting information in a body of text and returns a 
    description of the contradiction along with the relevant sentences and their 
    offsets within the original text.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.CONTRADICTION_DETECTION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str)->dict:
        self._args_dict = inspect_arguments(self.__call__, user, text)
        return super().__call__()
