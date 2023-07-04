from .node import NodeConfig
from soffosai.core.services import DocumentsIngestService, DocumentsSearchService, DocumentsDeleteService
from soffosai.core.services import inspect_arguments


class DocumentsIngestNodeConfig(NodeConfig):
    '''
    Ingest a text to Soffos' database, returns document_id that references that document
    '''
    def __init__(self, name:str, document_name:str, text:str=None, tagged_elements:list=None, meta:dict=None):
        source = inspect_arguments(self.__call__, document_name, text, tagged_elements, meta)
        service = DocumentsIngestService
        super().__init__(name, service, source)


class DocumentsSearchNodeConfig(NodeConfig):
    '''
    Return details about a document that was ingested to Soffos. 
    Takes document_ids, query, or filter.  Returns Passages of the documents and concatenated text.
    '''
    def __init__(self, name:str, query:str=None, filters:dict=None, document_ids:list=None, top_n_keywords:int=5,
        top_n_natural_language:int=5, date_from:str=None, date_until:str=None):
        source = inspect_arguments(self.__call__, query, filters, document_ids, top_n_keywords,
        top_n_natural_language, date_from, date_until)
        service = DocumentsSearchService
        super().__init__(name, service, source)


class DocumentsDeleteNodeConfig(NodeConfig):
    '''
    Deletes a document from the Soffos db that is referred to by the given document_ids
    '''
    def __init__(self, name:str, user:str, document_ids:list):
        source = inspect_arguments(self.__call__, user, document_ids)
        service = DocumentsDeleteService
        super().__init__(name, service, source)
