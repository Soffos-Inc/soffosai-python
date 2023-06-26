from .service_io import ServiceIO
from ..constants import ServiceString


class TagGenerationIO(ServiceIO):
    service = ServiceString.TAG_GENERATION
    required_input_fields = ["text"]
    optional_input_fields = ["options"]
    input_structure = {
        "text": str,
        "options": [str, str, str] # can only take a subset of ["one_word", "two_words", "three_words"]
    }
    output_structure = {
        "one_word": [
            {
                "text": str,
                "score": float
            },
            
        ],

        "two_words": [
            {
                "text": str,
                "score": float
            },

        ],

        "three_words": [
            {
                "text": str,
                "score": float
            },
        ]
    }
