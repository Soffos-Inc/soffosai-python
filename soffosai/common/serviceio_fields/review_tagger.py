'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2024-03-03
Purpose: Input/Output description for Review Tagger Service
-----------------------------------------------------
'''
from .service_io import ServiceIO
from ..constants import ServiceString


class ReviewTaggerIO(ServiceIO):
    service = ServiceString.REVIEW_TAGGER
    required_input_fields = ["text"]
    optional_input_fields = ["engine"]
    input_structure = {
        "engine": str, 
        "text": str
    }

    output_structure = {
        "engine": str,
        "object": str,
        "action": str,
        "fault": str
    }

