from .node import NodeConfig
from soffosai.core.services import inspect_arguments, QuestionAndAnswerGenerationService


class QuestionAndAnswerGenerationNodeConfig(NodeConfig):
    '''
    Question And Answer Generation Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str, sentence_split:int=3, sentence_overlap:bool=False):
        source = inspect_arguments(self.__call__, text, sentence_split, sentence_overlap)
        service = QuestionAndAnswerGenerationService
        super().__init__(name, service, source)
