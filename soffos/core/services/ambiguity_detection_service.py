'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-23
Purpose: Easily define Ambiguity Detection Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffos.common.constants import ServiceString


class AmbiguityDetectionService(SoffosAIService):
    '''
    A SoffosAIService that finds statements or sentences in text that are not coherent, 
    or can be interpreted in multiple ways while also taking in account the surrounding context.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.AMBIGUITY_DETECTION
        super().__init__(service, **kwargs)
    
    def __call__(
        self, 
        user = None,
        text=None,
        sentence_split=3,
        sentence_overlap=False,  
        **kwargs):

        self._args_dict = inspect_arguments(self.__call__, user, text, sentence_split, sentence_overlap, **kwargs)
        payload = self._args_dict
        return super().__call__()
