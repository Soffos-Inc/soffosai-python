'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use Documents Ingest, Search, and Delete Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString
from soffosai.common.service_io_map import SERVICE_IO_MAP
from soffosai.common.serviceio_fields import ServiceIO

class DocumentsIngestService(SoffosAIService):
    '''
    The Documents module enables ingestion of content into Soffos.
    Takes in the text and gives the document_id to reference the text in Soffos database
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.DOCUMENTS_INGEST
        super().__init__(service, **kwargs)
    
    def __call__(self, user, document_name, text=None, tagged_elements=None, meta=None):
        self._args_dict = inspect_arguments(self.__call__, user, document_name, text, tagged_elements, meta)
        self._args_dict['name'] = document_name
        self._args_dict.pop('document_name')
        return super().__call__()


class DocumentsSearchService(SoffosAIService):
    '''
    The Documents module enables search of ingested contents from Soffos.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.DOCUMENTS_SEARCH
        super().__init__(service, **kwargs)
    
    def __call__(self, user, query=None, filters=None, document_ids=None, top_n_keywords=None,
        top_n_natural_language=None, date_from=None, date_until=None):
        self._args_dict = inspect_arguments(self.__call__, user, query, filters, document_ids, top_n_keywords,
        top_n_natural_language, date_from, date_until)
        return super().__call__()


class DocumentsDeleteService(SoffosAIService):
    '''
    The Documents module enables deletion of ingested contents from Soffos.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.DOCUMENTS_DELETE
        super().__init__(service, **kwargs)
    
    def __call__(self, user, document_ids):
        self._args_dict = inspect_arguments(self.__call__, user, document_ids)
        return super().__call__()


class DocumentsService(SoffosAIService):
    '''
    The Documents module enables ingestion of content into Soffos.
    User can ingest text and get the reference to it as document_id.
    Cal also Retrieve the context and delete the ingested text from Soffos db.
    '''
    def __init__(self,  **kwargs) -> None:
        service = ServiceString.DOCUMENTS_SEARCH
        super().__init__(service, **kwargs)
    

    def __call__(self, user, query=None, filters=None, document_ids=None, top_n_keywords=None,
        top_n_natural_language=None, date_from=None, date_until=None):
        return self.search(user, query=query, filters=filters, document_ids=document_ids, top_n_keywords=top_n_keywords,
        top_n_natural_language=top_n_natural_language, date_from=date_from, date_until=date_until)

    
    def search(self, user, query=None, filters=None, document_ids=None, top_n_keywords=None,
        top_n_natural_language=None, date_from=None, date_until=None):
        self._service = ServiceString.DOCUMENTS_SEARCH
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.search, user, query, filters, document_ids, top_n_keywords,
        top_n_natural_language, date_from, date_until)
        return self.get_response(payload=self._args_dict)
    

    def ingest(self, user, document_name, text=None, tagged_elements=None, meta=None):
        self._service = ServiceString.DOCUMENTS_INGEST
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.ingest, user, document_name, text, tagged_elements, meta)
        self._args_dict['name'] = document_name
        self._args_dict.pop('document_name')
        return self.get_response(payload=self._args_dict)

    
    def delete(self, user, document_ids):
        self._service = ServiceString.DOCUMENTS_DELETE
        self._serviceio:ServiceIO = SERVICE_IO_MAP.get(self._service)
        self._args_dict = inspect_arguments(self.delete, user, document_ids)
        return self.get_response(payload=self._args_dict)
