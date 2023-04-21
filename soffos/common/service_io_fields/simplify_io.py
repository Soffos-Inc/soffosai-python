from .service_io import ServiceIO
from ..constants import Services


class SimplifyIO(ServiceIO):
    service = Services.SIMPLIFY
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "simplify": str
    }
