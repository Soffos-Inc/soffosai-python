'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-10-09
Purpose: Input/Output description for Ambiguity Detection Service
-----------------------------------------------------
'''
from .service_io import ServiceIO
from ..constants import ServiceString


class AmbiguityDetectionIO(ServiceIO):
    service = ServiceString.AMBIGUITY_DETECTION
    required_input_fields = ["text"]
    optional_input_fields = ["sentence_split","sentence_overlap"]
    input_structure = {
        "text": str, 
        "sentence_split": int, 
        "sentence_overlap": bool
    }

    output_structure = {
        "ambiguities": dict
    }


    @classmethod
    def special_validation(self, payload):
        
        if payload["sentence_split"] == 1 and payload["sentence_overlap"] == True:
            return False, 'Value "sentence_overlap" must be false when "sentence_split" is set to 1.'

        return super().special_validation(payload)