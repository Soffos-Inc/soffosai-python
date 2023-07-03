from .node import NodeConfig
from soffosai import FileConverterService, SummarizationService
from soffosai.core import NodeConfig, inspect_arguments

class FileConverterNodeConfig(NodeConfig):
    def __init__(self, user, file) -> None:
        service = FileConverterService
        source = inspect_arguments(self.__init__, user, file)
        super().__init__(service, source)


class SummarizerNodeConfig(NodeConfig):
    def __init__(self, user, text, sent_length) -> None:
        service = SummarizationService
        source = inspect_arguments(self.__init__, user, text, sent_length)
        super().__init__(service, source)

