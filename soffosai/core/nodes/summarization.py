from .node import Node
from soffosai.core.services import inspect_arguments, SummarizationService


class SummarizationNode(Node):
    '''
    Summarization Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str, sent_length:int):
        source = inspect_arguments(self.__init__, name, text, sent_length)
        service = SummarizationService
        super().__init__(name, service, source)
