from .node import NodeConfig
from soffosai.core.services import NamedEntityRecognitionService, inspect_arguments


class NERNodeConfig(NodeConfig):
    '''
    NER Service configuration for Pipeline Use
    '''
    def __init__(self, text:str, labels:dict=None):
        source = inspect_arguments(self.__call__, text, labels)
        service = NamedEntityRecognitionService
        super().__init__(service, source)
