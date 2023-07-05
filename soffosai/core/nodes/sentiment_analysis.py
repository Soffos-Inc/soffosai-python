from .node import Node
from soffosai.core.services import inspect_arguments, SentimentAnalysisService


class SentimentAnalysisNode(Node):
    '''
    Sentiment Analysis Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str, sentence_split:int=4, sentence_overlap:bool=False):
        source = inspect_arguments(self.__init__, name, text, sentence_split, sentence_overlap)
        service = SentimentAnalysisService
        super().__init__(name, service, source)
