from .service_io import ServiceIO
from ..constants import Services


class LogicalErrorDetectionIO(ServiceIO):
    service = Services.LOGICAL_ERROR_DETECTION
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "logical_errors": [
            {
            "text": str,
            "start": int,
            "end": int,
            "explanation": str
            },
            {
            "text": str,
            "start": int,
            "end": int,
            "explanation": str
            }
        ]
    }
