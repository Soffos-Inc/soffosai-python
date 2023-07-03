'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-27
Purpose: Easily use Table Generator Service
-----------------------------------------------------
'''
from typing import Union
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString

TABLE_FORMATS = ['markdonw', 'CSV']

class TableGeneratorService(SoffosAIService):
    '''
    The table generator module enables applications to extract numerical and statistical 
    data from raw text in a tabular format. For use-cases where data has to be manually 
    reviewed and cross-referenced, this module can bring enormous value.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.TABLE_GENERATOR
        super().__init__(service, **kwargs)
    

    def __call__(self, user:str, text:str, table_format:str='markdown'):
        if table_format not in TABLE_FORMATS:
            raise ValueError(f"The argument table_format accepted values are: {TABLE_FORMATS}")
        self._args_dict = inspect_arguments(self.__call__, user, text, table_format)
        return super().__call__()
