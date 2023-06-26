from .service_io import ServiceIO
from ..constants import ServiceString


class LanguageDetectionIO(ServiceIO):
    service = ServiceString.LANGUAGE_DETECTION
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "language": str
    }
