'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-17
Purpose: Handler of File Converter Service
-----------------------------------------------------
'''
import os
from .service import SoffosAIService
from soffos.common.constants import Services

class FileConverterService(SoffosAIService):
    '''
    For service description please go to:
    https://dev-platform.soffos.ai/playground/docs#/file-converter
    '''

    def __init__(self, apikey, user, normalize=0,src=None, concern=None, **kwargs) -> None:
        super().__init__(apikey, user, src, concern)
        self._normalize = normalize
        self._service = Services.FILE_CONVERTER
        

    def allow_input(self, source, concern):

        if isinstance(source, dict):
            self._document_id = source.get("document_id")
            source = source.get("file")
            if self._document_id:
                self._src = self._document_id
            else:
                self._src = source

        if not os.path.isfile(source):
            return False, "Please provide the correct path to the file"
        
        return True, None

    def provide_output_type(self):
        return str
    
    def provide_source_type(self):
        return str
    
    def provide_concern_type(self):
        return None
    
    def get_default_output_key(self):
        return "normalized_text"
    
    def get_default_secondary_output_key(self):
        return "text"

    def get_data(self):
        request_data = {
            "user": self._user,
            "normalize": self._normalize
        }

        return request_data
