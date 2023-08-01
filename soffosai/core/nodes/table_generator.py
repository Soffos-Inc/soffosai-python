from .node import Node
from soffosai.core.services import inspect_arguments, TableGeneratorService


TABLE_FORMATS = ['markdonw', 'CSV']

class TableGeneratorNode(Node):
    '''
    Table Generator Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str, table_format:str='markdown'):
        source = inspect_arguments(self.__init__, name, text, table_format)
        service = TableGeneratorService
        super().__init__(name, service, source)
