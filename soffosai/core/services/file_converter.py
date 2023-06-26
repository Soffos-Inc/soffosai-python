'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use File Converter Service
-----------------------------------------------------
'''
from typing import Union
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class FileConverterService(SoffosAIService):
    '''
    The File Converter extracts text from various types of files.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.FILE_CONVERTER
        super().__init__(service, **kwargs)
    
    def __call__(self, user, file, normalize:Union[None, int]=None):
        self._args_dict = inspect_arguments(self.__call__, user, file, normalize)
        return super().__call__()
