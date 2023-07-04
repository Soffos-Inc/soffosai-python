'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use Microlesson Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class MicrolessonService(SoffosAIService):
    '''
    Accepts a list of texts, each one labelled with its source and creates a concise microlesson 
    including a short summary, key points, learning objectives and tasks that aim to help the 
    learner achieve the learning objectives.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.MICROLESSON
        self.content = []
        super().__init__(service, **kwargs)
    

    def __call__(self, user:str, content:list=None):
        if content:
            self.content = content
        self._args_dict = inspect_arguments(self.__call__, user, content)
        self._args_dict['content'] = self.content
        return super().__call__()


    def add_content(self, source:str, text:str):
        '''
        Add content to the microlesson
        '''
        self.content.append(
            {
                "source": source,
                "text": text
            }
        )
