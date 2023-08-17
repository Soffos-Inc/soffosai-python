'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-27
Purpose: Easily use Sentiment Analysis Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class SentimentAnalysisService(SoffosAIService):
    '''
    This module processes the text to measure whether it is negative, positive or neutral. 
    The text is processed in segments of user-defined length and it provides scores for each 
    segment as well as the overall score of the whole text.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.SENTIMENT_ANALYSIS
        super().__init__(service, **kwargs)
    

    def __call__(self, user:str, text:str, sentence_split:int=4, sentence_overlap:bool=False):
        self._args_dict = inspect_arguments(self.__call__, user, text, sentence_split, sentence_overlap)
        return super().__call__()
