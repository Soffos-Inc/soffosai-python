from .service_io import ServiceIO
from ..constants import Services


class NamedEntityRecognitionIO(ServiceIO):
    service = Services.NER
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
