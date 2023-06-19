'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-17
Purpose: Handler of Ambiguity Detection Service
-----------------------------------------------------
'''
import os
from .service import SoffosAIService
from soffos.common.constants import ServiceString

class AmbiguityDetectionService(SoffosAIService):
    '''
    For service description please go to:
    https://dev-platform.soffos.ai/playground/docs#/ambiguity-detection
    '''

    def __init__(self, apikey, user, sentence_split=4, src=None, sentence_overlap=False, concern=None, **kwargs) -> None:
        super().__init__(apikey, user, src, concern)
        self._sentence_split = sentence_split
        self._service = ServiceString.AMBIGUITY_DETECTION
        self._sentence_overlap = sentence_overlap
        

    def provide_output_type(self):
        return list
    
    def provide_source_type(self):
        return str
    
    def provide_concern_type(self):
        return None
    
    def get_default_output_key(self):
        return "ambiguities"
    
    def get_default_secondary_output_key(self):
        return None

    def get_json(self):
        request_data = {
            "user": self._user,
            "text": self._src,
            "sentence_split": self._sentence_split,
            "sentence_overlap": self._sentence_overlap
        }

        return request_data
