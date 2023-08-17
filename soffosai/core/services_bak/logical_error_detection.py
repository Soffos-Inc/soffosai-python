'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use Logical Error Detection Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class LogicalErrorDetectionService(SoffosAIService):
    '''
    Identifies illogical statements in text and explains why they are illogical.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.LOGICAL_ERROR_DETECTION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str):
        self._args_dict = inspect_arguments(self.__call__, user, text)
        return super().__call__()
