from .service_io import ServiceIO
from ..constants import Services


class MicrolessonIO(ServiceIO):
    service = Services.MICROLESSON
    required_input_fields = ["content"]
    input_structure = {
    "content": [
            {
            "source": str,
            "text": str
            },
        ],
    "user": "b5601df8-6af3-4c1a-9ded-b7df4c506eab"
    }
    output_structure = {
        "microlesson": str
    }
