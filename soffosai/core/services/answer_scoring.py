'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use Answer Scoring Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class AnswerScoringService(SoffosAIService):
    '''
    This module will mark the user's answer based on the provided context, 
    the question and, optionally, the expected correct answer..
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.ANSWER_SCORING
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, context:str, question:str, user_answer:str, answer:str=None)->dict:
        self._args_dict = inspect_arguments(self.__call__, user, context, question, user_answer, answer)
        return super().__call__()
