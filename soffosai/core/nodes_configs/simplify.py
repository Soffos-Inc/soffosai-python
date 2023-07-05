from .node import NodeConfig
from soffosai.core.services import inspect_arguments, SimplifyService


class SimplifyNodeConfig(NodeConfig):
    '''
    Simplify Analysis Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str):
        source = inspect_arguments(self.__init__, name, text)
        service = SimplifyService
        super().__init__(name, service, source)
