from .node import Node
from soffosai.core.services import LogicalErrorDetectionService, inspect_arguments


class LogicalErrorDetectionNode(Node):
    '''
    Lets Discuss Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str):
        source = inspect_arguments(self.__init__, name, text)
        service = LogicalErrorDetectionService
        super().__init__(name, service, source)
