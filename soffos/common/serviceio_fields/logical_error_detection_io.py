from .service_io import ServiceIO
from ..constants import ServiceString


class LogicalErrorDetectionIO(ServiceIO):
    service = ServiceString.LOGICAL_ERROR_DETECTION
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
