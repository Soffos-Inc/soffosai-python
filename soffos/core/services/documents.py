'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-01
Purpose: Handler of Document Processing Service
-----------------------------------------------------
'''

from .service import SoffosAIService
from soffos.common.constants import ServiceString


class DocumentsIngestService(SoffosAIService):
    '''
    For service description please go to:
    https://dev-platform.soffos.ai/playground/docs#/documents
    '''

    def __init__(self, apikey, user, src={}, tagged_elements={},concern=None, **kwargs) -> None:
        super().__init__(apikey, user, src, concern)
        self._service = ServiceString.DOCUMENTS_INGEST
        self._tagged_elements = tagged_elements
        if not tagged_elements and "tagged_elements" in src.keys():
            self._tagged_elements = src['tagged_elements']
    
    def allow_input(self, source, concern):
        if not isinstance(source, self.provide_source_type()):
            return False, "Please provide a dictionary on your source"
        
        if not self._tagged_elements and "text" not in source.keys():
            return False, "Please provice either tagged_elements or text fields"

        if "tagged_elements" in source.keys() and "text" in source.keys():
            return False, "Only provide the text or tagged_elements field, not both"
        
        if "name" not in source.keys():
            return False, "Please provide the name field on the source <src>"

        # if "meta" not in source.keys():
        #     self._src['meta'] = {"name": source['name']} # just to provide default value for meta, this will be ignored

        return True, None

    def provide_source_type(self):
        return dict

    def provide_output_type(self):
        return str
    
    def provide_concern_type(self):
        return None
    
    def get_default_output_key(self):
        return "document_id"
    
    def get_default_secondary_output_key(self):
        return "success"
    
    def get_json(self):
        if self._tagged_elements:
            if 'meta' in self._src.keys():
                request_data = {
                    "user": self._user,
                    "name": self._src['name'],
                    "meta": self._src['meta'],
                    "tagged_elements": self._tagged_elements
                }
            else:
                request_data = {
                    "user": self._user,
                    "name": self._src['name'],
                    "tagged_elements": self._tagged_elements
                }
        
        else:
            if 'meta' in self._src.keys():
                request_data = {
                    "user": self._user,
                    "name": self._src['name'],
                    "meta": self._src['meta'],
                    "text": self._src['text']
                }
            else:
                request_data = {
                    "user": self._user,
                    "name": self._src['name'],
                    "text": self._src['text']
                }

        return request_data
    

class DocumentsSearchService(SoffosAIService):
    '''
    For service description please go to:
    https://dev-platform.soffos.ai/playground/docs#/documents
    '''

    def __init__(self, apikey, user, src=None, concern=None, **kwargs) -> None:
        super().__init__(apikey, user, src, concern)
        self._service = ServiceString.DOCUMENTS_SEARCH
        self._concern = concern
        if not isinstance(concern, dict):
            raise ValueError("concern should be a dictionary")
            
        if "query" not in concern.keys():
            self._concern['query'] = None

        if "document_ids" not in concern.keys():
            self._concern['document_ids'] = None

        if "filters" not in concern.keys():
            self._concern['filters'] = None
        
        if "top_n_keyword" not in concern.keys():
            self._concern["top_n_keyword"] = 5

        if "top_n_natural_language" not in concern.keys():
            self._concern["top_n_natural_language"] = 5
        
        if "date_from" not in concern.keys():
            self._concern['date_from'] = None

        if "date_until" not in concern.keys():
            self._concern['date_until'] = None

    
    def allow_input(self, source, concern):
        if not isinstance(concern, dict):
            return False, "The source or concern of this service expects a dictionary"

        if not self._concern["query"] and not self._concern["document_ids"] and not self._concern["filters"]:
            return False, "Please provide at least one of these keys: query, filters, document_ids"
            
        return True, None

    def provide_source_type(self):
        return dict

    def provide_output_type(self):
        return list
    
    def provide_concern_type(self):
        return dict
    
    def get_default_output_key(self):
        return "passages"
    
    def get_default_secondary_output_key(self):
        return None
    
    def get_json(self):

        request_data = {
                "user": self._user,
                "query": self._concern["query"],
                "document_ids": self._concern["document_ids"],
                "top_n_keyword": self._concern["top_n_keyword"],
                "top_n_natural_language": self._concern["top_n_natural_language"],
                "filters": self._concern["filters"],
                "date_from": self._concern["date_from"],
                "date_until": self._concern["date_until"]
            }
        return request_data


class DocumentsDeleteService(SoffosAIService):
    '''
    For service description please go to:
    https://dev-platform.soffos.ai/playground/docs#/documents
    '''

    def __init__(self, apikey, user, src=None, concern=None, **kwargs) -> None:
        super().__init__(apikey, user, src, concern)
        self._service = ServiceString.DOCUMENTS_DELETE
    
    def allow_input(self, source, concern):
        if not isinstance(concern, self.provide_concern_type()):
            return False, "Document Delete Service needs a list of document_ids as concern type"

        return True, None

    def provide_source_type(self):
        return list

    def provide_output_type(self):
        return bool
    
    def provide_concern_type(self):
        return list
    
    def get_default_output_key(self):
        return "success"
    
    def get_default_secondary_output_key(self):
        return None
    
    def get_json(self):
        request_data = {
                "user": self._user,
                "document_ids": self._concern
            }
        return request_data
