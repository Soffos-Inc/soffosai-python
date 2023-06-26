from .service_io import ServiceIO
from ..constants import ServiceString


class AmbiguityDetectionIO(ServiceIO):
    service = ServiceString.AMBIGUITY_DETECTION
    required_input_fields = ["text"]
    optional_input_fields = ["sentence_split", "sentence_overlap"]
    input_structure = {
        "text": str,
        "sentence_split": int,
        "sentence_overlap": bool
    }
    # output_fields = ["ambiguities"]
    output_structure = {
        "ambiguities": {
            "text": str,
            "span_start": int,
            "spane_end": int,
            "reason": str        
        }
    }
