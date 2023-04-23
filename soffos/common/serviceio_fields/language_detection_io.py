from .service_io import ServiceIO
from ..constants import Services


class LanguageDetectionIO(ServiceIO):
    service = Services.LANGUAGE_DETECTION
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "language": str
    }
