'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use Simplify Service
-----------------------------------------------------
'''
from typing import Union, Dict
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class SimplifyService(SoffosAIService):
    '''
    Paraphrase and Simplify are available as two different flavors of the same module. 
    While the Paraphrase module attempts to change the wording while keeping the same level of complexity, 
    the Simplify module outputs more commonly used words without altering the meaning of the original text. 
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.SIMPLIFY
        super().__init__(service, **kwargs)
    

    def __call__(self, user:str, text:str):
        self._args_dict = inspect_arguments(self.__call__, user, text)
        return super().__call__()


    def set_pipeline_input(self, ref_name:str, user:str, text:Union[str, Dict]) -> None:
        self.source_config = inspect_arguments(self.set_pipeline_input, ref_name, user, text)
        return super().set_pipeline_input()
