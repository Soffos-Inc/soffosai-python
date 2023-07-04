from .node import NodeConfig
from soffosai.core.services import MicrolessonService, inspect_arguments


class MicrolessonNodeConfig(NodeConfig):
    '''
    Microlesson Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, content:list):
        source = inspect_arguments(self.__call__, content)
        service = MicrolessonService
        super().__init__(name, service, source)
