from .node import Node
from soffosai.core.services import ContradictionDetectionService, inspect_arguments


class ContradictionDetectionNode(Node):
    '''
    Answer Scoring service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str):
        service = ContradictionDetectionService
        source = inspect_arguments(self.__init__, name, text)
        super().__init__(name, service, source)
