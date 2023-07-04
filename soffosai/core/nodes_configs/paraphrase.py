from .node import NodeConfig
from soffosai.core.services import inspect_arguments, ParaphraseService


class ParaphraseNodeConfig(NodeConfig):
    '''
    Paraphrase Service configuration for Pipeline Use
    '''
    def __init__(self, text:str):
        source = inspect_arguments(self.__call__, text)
        service = ParaphraseService
        super().__init__(service, source)
