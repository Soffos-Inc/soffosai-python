'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-27
Purpose: Easily use Tag Generation Service
-----------------------------------------------------
'''
from typing import Union, Dict
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class TagGenerationService(SoffosAIService):
    '''
    This module can generate tags for a piece of text that can aid with content search in 
    certain use-cases. It allows to specify a number of tags to be generated for each of 
    the categories "topic", "domain", "audience", "entity".
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.TAG_GENERATION
        super().__init__(service, **kwargs)
    

    def __call__(self, user:str, text:str, types:list=["topic"], n:int=10):
        '''
        Note: List of types of keywords to extract. Supported types:

        topic: Tags relating to the subject matter of the text. 
        domain: Tags relating to the domain of the text. For example, "AI", or "Science fiction". 
            In some cases, domain tags might be similar to topic tags. 
        audience: Tags relating to the type of audience the text is intended for. 
        entity: Entities such as people, places, products, etc. mentioned in the text.
        '''
        for _type in types:
            if _type not in ["topic", "domain", "audience", "entity"]:
                raise ValueError(f'{self._service} types argument\'s elements can only be "topic", "domain", "audience" and/or "entity".')
        self._args_dict = inspect_arguments(self.__call__, user, text, types, n)
        return super().__call__()


    def set_pipeline_input(self, ref_name:str, user:str, text:Union[str, Dict], types:Union[list, Dict]=["topic"], n:Union[int, Dict]=10) -> None:
        self.source_config = inspect_arguments(self.set_pipeline_input, ref_name, user, text, types, n)
        return super().set_pipeline_input()
