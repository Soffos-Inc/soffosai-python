from .node import NodeConfig
from soffosai.core.services import LogicalErrorDetectionService, inspect_arguments


class LogicalErrorDetectionNodeConfig(NodeConfig):
    '''
    Lets Discuss Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str):
        source = inspect_arguments(self.__call__, text)
        service = LogicalErrorDetectionService
        super().__init__(name, service, source)
