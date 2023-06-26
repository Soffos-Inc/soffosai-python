from .service_io import ServiceIO
from ..constants import ServiceString


class ProfanityIO(ServiceIO):
    service = ServiceString.PROFANITY
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "profanities": [
            {
                "text": str,
                "span_start": int,
                "span_end": int
            }
        ],
        "offensive_probability": float,
        "offensive_prediction": bool
    }
