'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-01
Purpose: Handler of Contradiction Detection Service
-----------------------------------------------------
'''

from .service import SoffosAIService
from soffos.common.constants import Services

class ContradictionDetectionService(SoffosAIService):
    '''
    For service description please go to:
    https://dev-platform.soffos.ai/playground/docs#/contradiction-detection
    '''

    def __init__(self, apikey, user, src=None, concern=None, **kwargs) -> None:
        super().__init__(apikey, user, src, concern)
        self._service = Services.CONTRADICTION_DETECTION
        

    def allow_input(self, source, concern):
        if isinstance(source, dict):
            source = source.get("text")
        if not source:
            return False, "The provided src dictionary does not have the required field 'text'."
        if not isinstance(source, self.provide_source_type()):
            return False, "Please provide a string datatype on your src."
        
        return True, None

    def provide_source_type(self):
        return str
    
    def provide_output_type(self):
        return list
    
    def provide_concern_type(self):
        return None
    
    def get_default_output_key(self):
        return "contradictions"
    
    def get_default_secondary_output_key(self):
        return None
    
    def get_json(self):
        request_data = {
                "user": self._user,
                "text": self._src
            }
        return request_data
