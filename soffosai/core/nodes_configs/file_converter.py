from .node import NodeConfig
from soffosai.core.services import FileConverterService, SummarizationService, inspect_arguments
from soffosai.core.nodes_configs.node import NodeConfig


class FileConverterNodeConfig(NodeConfig):
    def __init__(self, name:str, file) -> None:
        service = FileConverterService
        source = inspect_arguments(self.__init__, file)
        super().__init__(name, service, source)
