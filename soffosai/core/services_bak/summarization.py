'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-27
Purpose: Easily use Summarization Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class SummarizationService(SoffosAIService):
    '''
    The summarization module utilizes Natural Language Generation (NLG) to generate an 
    abstractive summary of a specified length. In contrast to extractive summarization methods, 
    which simply calculate the centrality of sentences or passages in the original text and 
    concatenate the highest rated ones, abstractive summaries are often more concise and accurate. 
    The end result isn't necessarily a sum of word-for-word copies of passages from the original text, 
    but a combination of all key points formulated as a new text.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.SUMMARIZATION
        super().__init__(service, **kwargs)
    

    def __call__(self, user:str, text:str, sent_length:int):
        self._args_dict = inspect_arguments(self.__call__, user, text, sent_length)
        return super().__call__()
