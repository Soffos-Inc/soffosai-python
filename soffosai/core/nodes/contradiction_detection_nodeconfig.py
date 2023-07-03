from .node import NodeConfig
from soffosai.core.services import ContradictionDetectionService, inspect_arguments


class ContradictionDetectionNodeConfig(NodeConfig):
    '''
    Answer Scoring service configuration for Pipeline Use
    '''
    def __init__(self, text:str):
        service = ContradictionDetectionService
        source = inspect_arguments(self.__init__, text)
        super().__init__(service, source)
