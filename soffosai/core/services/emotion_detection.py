'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use Emotion Detection Service
-----------------------------------------------------
'''
from typing import Union, Dict
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString

_EMOTION_LIST = ["joy", "trust", "fear", "surprise", "sadness", "disgust", "anger", "anticipation"]

class EmotionDetectionService(SoffosAIService):
    '''
    Detect selected emotions within the provided text. The original text is chunked to 
    passages of a specified sentence length. Smaller chunks yield better accuracy.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.EMOTION_DETECTION
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str, sentence_split:int=4, sentence_overlap:bool=False, emotion_choices:list=_EMOTION_LIST):
        for emotion in emotion_choices:
            if emotion not in _EMOTION_LIST:
                raise ValueError(f"{emotion} is not valid as an emotion_choices element. Please choose from {_EMOTION_LIST}.")
        self._args_dict = inspect_arguments(self.__call__, user, text, sentence_split, sentence_overlap, emotion_choices)
        return super().__call__()


    def set_pipeline_input(self, ref_name:str, text:Union[str, Dict], sentence_split:Union[int, Dict]=4, sentence_overlap:Union[bool, Dict]=False, emotion_choices:Union[list, Dict]=_EMOTION_LIST) -> None:
        self.source_config = inspect_arguments(self.set_pipeline_input, ref_name, text, sentence_split, sentence_overlap, emotion_choices)
        return super().set_pipeline_input()
