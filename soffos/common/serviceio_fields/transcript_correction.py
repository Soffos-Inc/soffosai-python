from .service_io import ServiceIO
from ..constants import ServiceString


class TranscriptCorrectionIO(ServiceIO):
    service = ServiceString.TRANSCRIPTION_CORRECTION
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "correction": str
    }
