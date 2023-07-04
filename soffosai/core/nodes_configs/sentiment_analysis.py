from .node import NodeConfig
from soffosai.core.services import inspect_arguments, SentimentAnalysisService


class SentimentAnalysisNodeConfig(NodeConfig):
    '''
    Sentiment Analysis Service configuration for Pipeline Use
    '''
    def __init__(self, text:str, sentence_split:int=4, sentence_overlap:bool=False):
        source = inspect_arguments(self.__call__, text, sentence_split, sentence_overlap)
        service = SentimentAnalysisService
        super().__init__(service, source)
