from .node import Node
from soffosai.core.services import inspect_arguments, TagGenerationService


class TagGenerationNode(Node):
    '''
    Tag Generation Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str, types:list=["topic"], n:int=10):
        source = inspect_arguments(self.__init__, name, text, types, n)
        service = TagGenerationService
        super().__init__(name, service, source)
