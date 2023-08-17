'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-23
Purpose: Easily use Ambiguity Detection Service
-----------------------------------------------------
'''
from typing import Union, Dict
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class AmbiguityDetectionService(SoffosAIService):
    '''
    A SoffosAIService that finds statements or sentences in text that are not coherent, 
    or can be interpreted in multiple ways while also taking in account the surrounding context.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.AMBIGUITY_DETECTION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str, sentence_split:int=4, sentence_overlap:bool=False) -> dict:
        '''
        :param user: The identify of the user sending this request. The user of the app.
        :param text: Text to be analyzed for ambiguitites.
        :param sentence_split: The number of sentences of each chunk when splitting the input text.
        :param sentence_overlap: Whether to overlap adjacent chunks by 1 sentence. 
                                For example, with sentence_split 3 and sentence_overlap=true :
                                [[s1, s2, s3], [s3, s4, s5], [s5, s6, s7]]
        '''
        self._args_dict = inspect_arguments(self.__call__, user, text, sentence_split, sentence_overlap)
        return super().__call__()


    def set_pipeline_input(self, ref_name:str, text:Union[str, Dict], sentence_split:Union[int, Dict]=4, sentence_overlap:Union[bool, Dict]=False) -> None:
        self.source_config = inspect_arguments(self.set_pipeline_input, ref_name, text, sentence_split, sentence_overlap)
        return super().set_pipeline_input()

