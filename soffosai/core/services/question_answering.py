'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-27
Purpose: Easily use Question Answering Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class QuestionAnsweringService(SoffosAIService):
    '''
    This module is a combination of various sub-modules that enable users to get accurate answers on 
    questions posed on a large amount of content. It includes basic intent recognition capabilities 
    to enable appropriate responses to incorrect or profane language, or typical personal questions 
    like "How are you?" and greetings
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.QUESTION_ANSWERING
        super().__init__(service, **kwargs)
    

    def __call__(self, user:str, question:str, document_text:str=None, document_ids:list=None, 
        check_ambiguity:bool=True, check_query_type:bool=True, generic_response:bool=False, meta:dict=None):
        self._args_dict = inspect_arguments(self.__call__, user, question, document_text, document_ids, 
        check_ambiguity, check_query_type, generic_response, meta)
        self._args_dict['message'] = question
        return super().__call__()

