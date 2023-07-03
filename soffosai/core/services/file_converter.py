'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use File Converter Service
-----------------------------------------------------
'''
from typing import Union
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


_NORMALIZE_VALUES = [0, 1]

class FileConverterService(SoffosAIService):
    '''
    The File Converter extracts text from various types of files.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.FILE_CONVERTER
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, file:str, normalize:int=0):
        if normalize not in _NORMALIZE_VALUES:
            raise ValueError(f"{self._service}: normalize can only accept a value of 0 or 1")
        self._args_dict = inspect_arguments(self.__call__, user, file, normalize)
        return super().__call__()
