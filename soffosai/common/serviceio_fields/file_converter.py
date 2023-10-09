'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-10-09
Purpose: Input/Output description for File Converter Service
-----------------------------------------------------
'''
from .service_io import ServiceIO
from ..constants import ServiceString
from io import BufferedReader


class FileConverterIO(ServiceIO):
    service = ServiceString.FILE_CONVERTER
    required_input_fields = ["file","normalize"]
    optional_input_fields = []
    input_structure = {
        # "file": (BufferedReader, str), 
        "normalize": str
    }

    output_structure = {
        "normalize": str,
        "text": str,
        "tagged_elements": dict,
        "normalized_text": str,
        "normalized_tagged_elements": dict
    }

