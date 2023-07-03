from .node import NodeConfig
from soffosai.core.services import FileConverterService, SummarizationService, inspect_arguments
from soffosai.core.nodes.node import NodeConfig

class FileConverterNodeConfig(NodeConfig):
    def __init__(self, file) -> None:
        service = FileConverterService
        source = inspect_arguments(self.__init__, file)
        super().__init__(service, source)


class SummarizationNodeConfig(NodeConfig):
    def __init__(self, text, sent_length) -> None:
        service = SummarizationService
        source = inspect_arguments(self.__init__, text, sent_length)
        super().__init__(service, source)

