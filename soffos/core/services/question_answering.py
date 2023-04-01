'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-01
Purpose: The main module of Soffos
-----------------------------------------------------
'''

from .service import SoffosAIService
from soffos.common.constants import Services

class QuestionAnsweringService(SoffosAIService):

    def __init__(self, apikey, output_key=None, source=None, question=None) -> None:
        super().__init__(apikey, output_key, source)
        self._question = question
        self._service = Services.QUESTION_ANSWERING
        

    def allow_input(self, value):
        if not isinstance(value, str):
            return False, str
        
        return True, str

    def provide_output_type(self):
        return str
    
    def get_default_output_key(self):
        return "answer"
    
    def get_json(self):
        return {
                "user": self._apikey,
                "message": self._question,
                "document_text": self._source
            }