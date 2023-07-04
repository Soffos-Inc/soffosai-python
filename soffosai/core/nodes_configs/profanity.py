from .node import NodeConfig
from soffosai.core.services import inspect_arguments, ProfanityService


class ProfanityNodeConfig(NodeConfig):
    '''
    Profanity Service configuration for Pipeline Use
    '''
    def __init__(self, text:str):
        source = inspect_arguments(self.__call__, text)
        service = ProfanityService
        super().__init__(service, source)
