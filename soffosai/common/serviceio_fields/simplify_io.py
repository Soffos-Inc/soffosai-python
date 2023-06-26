from .service_io import ServiceIO
from ..constants import ServiceString


class SimplifyIO(ServiceIO):
    service = ServiceString.SIMPLIFY
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "simplify": str
    }
