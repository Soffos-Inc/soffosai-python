from .service_io import ServiceIO
from ..constants import Services


class ProfanityIO(ServiceIO):
    service = Services.PROFANITY
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
