'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use Language Detection Service
-----------------------------------------------------
'''
from typing import Union, Dict
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class LanguageDetectionService(SoffosAIService):
    '''
    The Language Detection module detects the dominant language in the provided text.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.LANGUAGE_DETECTION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str):
        self._args_dict = inspect_arguments(self.__call__, user, text)
        return super().__call__()


    def set_pipeline_input(self, ref_name:str, text:Union[str, Dict]) -> None:
        self.source_config = inspect_arguments(self.set_pipeline_input, ref_name, text)
        return super().set_pipeline_input()
