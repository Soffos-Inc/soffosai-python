from .node import NodeConfig
from soffosai.core.services import LetsDiscussService, inspect_arguments
from soffosai.core.services import LetsDiscussCreateService, LetsDiscussRetrieveService, LetsDiscussDeleteService


class LetsDiscussNodeConfig(NodeConfig):
    '''
    Lets Discuss Service configuration for Pipeline Use
    '''
    def __init__(self, session_id:str, query:str):
        source = inspect_arguments(self.__call__, session_id, query)
        service = LetsDiscussService
        super().__init__(service, source)


class LetsDiscussCreateNodeConfig(NodeConfig):
    '''
    Lets Discuss Create Service configuration for Pipeline Use
    '''
    def __init__(self, context:str):
        source = inspect_arguments(self.__call__, context)
        service = LetsDiscussCreateService
        super().__init__(service, source)


class LetsDiscussRetrieveNodeConfig(NodeConfig):
    '''
    Lets Discuss Retrieve Sessions Service configuration for Pipeline Use
    '''
    def __init__(self, return_messages:bool):
        source = inspect_arguments(self.__call__, return_messages)
        service = LetsDiscussRetrieveService
        super().__init__(service, source)


class LetsDiscussDeleteNodeConfig(NodeConfig):
    '''
    Lets Discuss Delete Sessions Service configuration for Pipeline Use
    '''
    def __init__(self, return_messages:bool):
        source = inspect_arguments(self.__call__, return_messages)
        service = LetsDiscussDeleteService
        super().__init__(service, source)
