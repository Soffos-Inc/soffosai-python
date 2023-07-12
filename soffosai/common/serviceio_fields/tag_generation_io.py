from .service_io import ServiceIO
from ..constants import ServiceString


class TagGenerationIO(ServiceIO):
    service = ServiceString.TAG_GENERATION
    required_input_fields = ["text"]
    optional_input_fields = ["types", "n"]
    input_structure = {
        "text": str,
        "types": [str, str, str], # can only take a subset of ["topic", "domain", "audience", "entity"]
        "n": int 
    }
    output_structure = {
        "tags": {
            "label1": [
                {
                    "tag": str,
                    "score": float
                },
                {
                    "tag": str,
                    "score": float
                }
            ],
            "label2": [
                {
                    "tag": str,
                    "score": float
                },
                {
                    "tag": str,
                    "score": float
                }
            ],
        }
    }
