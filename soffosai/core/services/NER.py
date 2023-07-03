'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use NamedEntityRecognition Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class NamedEntityRecognitionService(SoffosAIService):
    '''
    Identifies named entities in text. It supports custom labels.
    This module is extremely versatile as the labels can be defined by the user. 
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.NER
        self.labels = {}
        super().__init__(service, **kwargs)
    

    def __call__(self, user:str, text:str, labels:dict=None):
        
        self._args_dict = inspect_arguments(self.__call__, user, text, labels)

        if not labels and len(self.labels.keys()) > 0:
            self._args_dict['labels'] = self.labels

        return super().__call__()


    def add_label(self, label:str, definition:str):
        '''
        Adds a TAG label and its description so that Soffos AI can identify the entities matching the tag
        '''
        self.labels[label] = definition
        