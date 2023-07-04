from .node import NodeConfig
from soffosai.core.services import inspect_arguments, SummarizationService


class SummarizationNodeConfig(NodeConfig):
    '''
    Summarization Service configuration for Pipeline Use
    '''
    def __init__(self, text:str, sent_length:int):
        source = inspect_arguments(self.__call__, text, sent_length)
        service = SummarizationService
        super().__init__(service, source)
