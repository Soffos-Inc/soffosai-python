'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-27
Purpose: Easily use Review Tagger Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class ReviewTaggerService(SoffosAIService):
    '''
    This module extracts key information from negative product reviews. It attempts to find 
    the referred object, it's fault and an action/verb that is associated with it. If any 
    of the information is not present, it returns "n/a". This is useful for organizations who 
    want to analyze product reviews in order to identify and prioritize the most important issues.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.REVIEW_TAGGER
        super().__init__(service, **kwargs)
    

    def __call__(self, user:str, text:str):
        self._args_dict = inspect_arguments(self.__call__, user, text)
        return super().__call__()
