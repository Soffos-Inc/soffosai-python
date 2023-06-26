'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use Emotion Detection Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class EmotionDetectionService(SoffosAIService):
    '''
    Detect selected emotions within the provided text. The original text is chunked to 
    passages of a specified sentence length. Smaller chunks yield better accuracy.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.EMOTION_DETECTION
        super().__init__(service, **kwargs)
    
    def __call__(self, user, text):
        self._args_dict = inspect_arguments(self.__call__, user, text)
        return super().__call__()
