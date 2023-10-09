'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-10-09
Purpose: Easily use Ambiguity Detection Service
-----------------------------------------------------
'''
from .service import SoffosAIService
from .input_config import InputConfig
from soffosai.common.constants import ServiceString
from typing import Union



class AmbiguityDetectionService(SoffosAIService):
    '''
    This module finds statements or sentences in text that are not coherent, or can
    be interpreted in multiple ways while also taking in account the surrounding
    context. For example, "The fisherman went to the bank" would be identified as
    ambiguous, but "The fisherman went to the bank to draw money" won't. It accepts
    parameters to control the way the text is segmented for processing. It gives an
    explanation as to why a span of text is considered ambiguous. Despite taking in
    account the context of each span, the module may sometimes be strict in what it
    considers ambiguous, even if the combination of words mean something very
    specific most of the time. A very fascinating tool for writers that can be used
    to inspire, write more understandable content, or even to just delve into the
    remarkable nuances and complexities hidden in human language and thought
    '''

    def __init__(self, **kwargs) -> None:
        service = ServiceString.AMBIGUITY_DETECTION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str, sentence_split:int=4, sentence_overlap:bool=None) -> dict:
        '''
        Call the Ambiguity Detection Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be analyzed for ambiguities.
        :param sentence_split: The number of sentences of each chunk when splitting the input text.
        :param sentence_overlap: Whether to overlap adjacent chunks by 1 sentence. For example, with
            sentence_split=3 and sentence_overlap=true : [[s1, s2, s3], [s3, s4, s5],
            [s5, s6, s7]]
        :return: ambiguities: A list of dictionaries. Each dictionary represents an ambiguity and
            contains the following fields: text: The text classified as ambiguous.
            span_start: The starting character index of the ambiguous text in the
            original text. span_end: The ending character index of the ambiguous text
            in the original text. reason: An explanation on why the span is considered
            ambiguous.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/ambiguity_detection.py>`_
        '''
        return super().__call__(user=user, text=text, sentence_split=sentence_split, sentence_overlap=sentence_overlap)

    def set_input_configs(self, name:str, text:Union[str, InputConfig], sentence_split:Union[int, InputConfig]=4, sentence_overlap:Union[bool, InputConfig]=None):
        super().set_input_configs(name=name, text=text, sentence_split=sentence_split, sentence_overlap=sentence_overlap)

    @classmethod
    def call(self, user:str, text:str, sentence_split:int=4, sentence_overlap:bool=None) -> dict:
        '''
        Call the Ambiguity Detection Service
        
        :param user: The ID of the user accessing the Soffos API.
            Soffos assumes that the owner of the api is an application (app) and that app has users.
            Soffos API will accept any string."
        
        :param text: Text to be analyzed for ambiguities.
        :param sentence_split: The number of sentences of each chunk when splitting the input text.
        :param sentence_overlap: Whether to overlap adjacent chunks by 1 sentence. For example, with
            sentence_split=3 and sentence_overlap=true : [[s1, s2, s3], [s3, s4, s5],
            [s5, s6, s7]]
        :return: ambiguities: A list of dictionaries. Each dictionary represents an ambiguity and
            contains the following fields: text: The text classified as ambiguous.
            span_start: The starting character index of the ambiguous text in the
            original text. span_end: The ending character index of the ambiguous text
            in the original text. reason: An explanation on why the span is considered
            ambiguous.
        :Examples
        Detailed examples can be found at `Soffos Github Repository <https://github.com/Soffos-Inc/soffosai-python/tree/master/samples/services/ambiguity_detection.py>`_
        '''
        return super().call(user=user, text=text, sentence_split=sentence_split, sentence_overlap=sentence_overlap)

