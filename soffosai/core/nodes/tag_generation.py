from .node import Node
from soffosai.core.services import inspect_arguments, TagGenerationService


class TagGenerationNode(Node):
    '''
    Tag Generation Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str, types:list=["topic"], n:int=10):
        for _type in types:
            if _type not in ["topic", "domain", "audience", "entity"]:
                raise ValueError(f'Tag Generation: types argument\'s elements can only be "topic", "domain", "audience" and/or "entity".')
        source = inspect_arguments(self.__init__, name, text, types, n)
        service = TagGenerationService
        super().__init__(name, service, source)
