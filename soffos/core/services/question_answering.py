'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-01
Purpose: The main module of Soffos
-----------------------------------------------------
'''

from .service import SoffosAIService
from soffos.common.constants import Services

class QuestionAnsweringService(SoffosAIService):

    def __init__(self, apikey, src=None, concern=None) -> None:
        super().__init__(apikey, src, concern)
        self._question = concern
        self._service = Services.QUESTION_ANSWERING
        

    def allow_input(self, source, concern):
        if not isinstance(source, self.provide_source_type()):
            return False, "Please provide string datatype on your source"
        
        if not isinstance(concern, self.provide_concern_type()):
            return False, "Please provide string datatype on your question/concern"
        
        return True, str

    def provide_output_type(self):
        return str
    
    def provide_source_type(self):
        return str
    
    def provide_concern_type(self):
        return str
    
    def get_default_output_key(self):
        return "answer"
    
    def get_json(self):
        return {
                "user": self._apikey,
                "message": self._question,
                "document_text": self._src
            }
