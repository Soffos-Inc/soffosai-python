from .service_io import ServiceIO
from ..constants import Services


class TranscriptCorrectionIO(ServiceIO):
    service = Services.TRANSCRIPTION_CORRECTION
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "correction": str
    }
