from .node import Node
from soffosai.core.services import NamedEntityRecognitionService, inspect_arguments


class NERNode(Node):
    '''
    NER Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str, labels:dict=None):
        source = inspect_arguments(self.__init__, name, text, labels)
        service = NamedEntityRecognitionService
        super().__init__(name, service, source)
