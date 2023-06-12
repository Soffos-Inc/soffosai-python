'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-01
Purpose: Handler of Question Answering Service
-----------------------------------------------------
'''

from .service import SoffosAIService
from soffos.common.constants import ServiceString

class QuestionAnsweringService(SoffosAIService):
    '''
    For service description please go to:
    https://dev-platform.soffos.ai/playground/docs#/question-answering
    '''

    def __init__(self, user, src=None, document_ids=None, concern=None, document_text=None,**kwargs) -> None:
        self._question = concern
        self._service = ServiceString.QUESTION_ANSWERING
        self._document_ids = document_ids
        self._document_text = document_text
        self._src = src
        super().__init__(user, src, concern)

    def allow_input(self, source, concern):

        if isinstance(source, dict):
            self.src = self._src
            if "document_id" in source.keys():
                self._document_id = source['document_id']
                
            if not concern:
                concern = source.get("question")
            if not concern:
                concern = source.get("message")

            self._question = concern
            source = source.get("text") if source.get("text") else source.get("document_text")
        
        if not source and not self._document_ids:
            return False, "src is not specified."

        if not isinstance(source, self.provide_source_type()):
            return False, "Please provide string datatype on your source"
        
        if not isinstance(concern, self.provide_concern_type()):
            return False, "Please provide string datatype on your question/concern"
        
        self._src = source
        return True, None

    def provide_output_type(self):
        return str
    
    def provide_source_type(self):
        return str
    
    def provide_concern_type(self):
        return str
    
    def get_default_output_key(self):
        return "answer"
    
    def get_default_secondary_output_key(self):
        return None
    
    def get_json(self):
        # if self.src:
        #     return self.src
        if self._document_ids:
            request_data = {
                "user": self._user,
                "message": self._question,
                "document_id": self._document_ids
            }
        else:
            request_data = {
                "user": self._user,
                "message": self._question,
                "document_text": self._src
            }
        
        return request_data
