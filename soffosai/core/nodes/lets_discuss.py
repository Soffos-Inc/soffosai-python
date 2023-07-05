from .node import Node
from soffosai.core.services import LetsDiscussService, inspect_arguments
from soffosai.core.services import LetsDiscussCreateService, LetsDiscussRetrieveService, LetsDiscussDeleteService


class LetsDiscussNode(Node):
    '''
    Lets Discuss Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, session_id:str, query:str):
        source = inspect_arguments(self.__init__, name, session_id, query)
        service = LetsDiscussService
        super().__init__(name, service, source)


class LetsDiscussCreateNode(Node):
    '''
    Lets Discuss Create Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, context:str):
        source = inspect_arguments(self.__init__, name, context)
        service = LetsDiscussCreateService
        super().__init__(name, service, source)


class LetsDiscussRetrieveNode(Node):
    '''
    Lets Discuss Retrieve Sessions Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, return_messages:bool):
        source = inspect_arguments(self.__init__, name, return_messages)
        service = LetsDiscussRetrieveService
        super().__init__(name, service, source)


class LetsDiscussDeleteNode(Node):
    '''
    Lets Discuss Delete Sessions Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, return_messages:bool):
        source = inspect_arguments(self.__init__, name, return_messages)
        service = LetsDiscussDeleteService
        super().__init__(name, service, source)
