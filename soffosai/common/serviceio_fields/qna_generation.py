'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2024-03-03
Purpose: Input/Output description for Qn A Generation Service
-----------------------------------------------------
'''
from .service_io import ServiceIO
from ..constants import ServiceString


class QnAGenerationIO(ServiceIO):
    service = ServiceString.QN_A_GENERATION
    required_input_fields = ["text"]
    optional_input_fields = ["engine","sentence_split","sentence_overlap"]
    input_structure = {
        "engine": str, 
        "text": str, 
        "sentence_split": int, 
        "sentence_overlap": bool
    }

    output_structure = {
        "engine": str,
        "qna_list": dict,
        "chunks": dict
    }


    @classmethod
    def special_validation(self, payload):
        
        if payload["sentence_split"] == 1 and payload["sentence_overlap"] == True:
            return False, 'Value "sentence_overlap" must be false when "sentence_split" is set to 1.'

        return super().special_validation(payload)