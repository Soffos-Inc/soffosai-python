from .service_io import ServiceIO
from ..constants import ServiceString


class SummarizaionIO(ServiceIO):
    service = ServiceString.SUMMARIZATION
    required_input_fields = ["sent_length", "text"]
    input_structure = {
        "sent_length": int,
        "text": str
    }
    output_structure = {
        "summary": str
    }
