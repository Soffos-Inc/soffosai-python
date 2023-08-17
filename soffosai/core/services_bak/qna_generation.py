'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-27
Purpose: Easily use Question and Answer Generation Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class QuestionAndAnswerGenerationService(SoffosAIService):
    '''
    The Q&A Generation module splits large documents in chunks from which it generates multiple 
    question-answer pairs. The chunk length is configurable. Usually more questions can be generated 
    when segmenting the text to smaller chunks, while longer chunks help retain more context, in cases 
    where a topic is discussed over multiple sentences in the context. To address cases where the topic 
    is split mid-way, the module supports overlapping the chunks by a configurable amount of sentences. 
    This gives a lot of flexibility to cater to your specific use case.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.QUESTION_AND_ANSWER_GENERATION
        super().__init__(service, **kwargs)
    

    def __call__(self, user:str, text:str, sentence_split:int=3, sentence_overlap:bool=False):
        self._args_dict = inspect_arguments(self.__call__, user, text, sentence_split, sentence_overlap)
        return super().__call__()
