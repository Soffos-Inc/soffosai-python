'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-27
Purpose: Easily use Transcript Correction Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class TranscriptCorrectionService(SoffosAIService):
    '''
    This module cleans up and corrects poorly transcribed text from Speech-To-Text (STT) systems. 
    It can handle cases where STT produced the wrong word or phrase by taking into account the 
    surrounding context and choosing the most fitting replacement. Although this is meant for correcting 
    STT outpus, it can also be used to correct grammar, misspellings and syntactical errors.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.TRANSCRIPTION_CORRECTION
        super().__init__(service, **kwargs)
    

    def __call__(self, user:str, text:str):
        self._args_dict = inspect_arguments(self.__call__, user, text)
        return super().__call__()
