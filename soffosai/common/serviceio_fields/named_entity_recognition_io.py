from .service_io import ServiceIO
from ..constants import ServiceString


class NamedEntityRecognitionIO(ServiceIO):
    service = ServiceString.NER
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "named_entities": [
            {
                "span": [
                    int,
                    int
                ],
                "tag": str,
                "text": str
            },
            {
                "span": [
                    int,
                    int
                ],
                "tag": str,
                "text": str
            },
        ]
    }
