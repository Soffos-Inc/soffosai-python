from .node import NodeConfig
from soffosai.core.services import AmbiguityDetectionService, inspect_arguments


class AmbiguityDetectionNodeConfig(NodeConfig):
    '''
    Ambiguity Detection service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str, sentence_split:int=4, sentence_overlap=False):
        service = AmbiguityDetectionService
        source = inspect_arguments(self.__init__, name, text, sentence_split, sentence_overlap)
        super().__init__(name, service, source)
