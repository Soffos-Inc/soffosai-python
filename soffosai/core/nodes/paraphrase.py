from .node import Node
from soffosai.core.services import inspect_arguments, ParaphraseService


class ParaphraseNode(Node):
    '''
    Paraphrase Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str):
        source = inspect_arguments(self.__init__, name, text)
        service = ParaphraseService
        super().__init__(name, service, source)
