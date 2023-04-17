'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-04-01
Purpose: Handler of Question Answering Service
-----------------------------------------------------
'''
import os
import mimetypes
from .service import SoffosAIService
from soffos.common.constants import Services

class FileConverterService(SoffosAIService):

    def __init__(self, apikey, user, src=None, concern=None) -> None:
        super().__init__(apikey, user, src, concern)
        self._question = concern
        self._service = Services.FILE_CONVERTER
        

    def allow_input(self, source, concern):

        if not os.path.isfile(source):
            return False, "Please provide the correct path to the file"
        
        return True, str

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
            "user": self._user
        }

        return request_data
