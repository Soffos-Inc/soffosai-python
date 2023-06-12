from .service_io import ServiceIO
from ..constants import ServiceString

class FileConverterIO(ServiceIO):
    service = ServiceString.FILE_CONVERTER
    required_input_fields = ["file"]
    optional_input_fields = ["normalize"]
    input_structure = {
        "file": str,
        "normalize": int
    }
    output_structure = {
        "text": str,
        "tagged_elements": [
            {
            "text": str,
            "tag": str
            },
        ]
    }
