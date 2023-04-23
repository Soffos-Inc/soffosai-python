from .service_io import ServiceIO
from ..constants import Services


class SummarizaionIO(ServiceIO):
    service = Services.SUMMARIZATION
    required_input_fields = ["sent_length", "text"]
    input_structure = {
        "sent_length": int,
        "text": str
    }
    output_structure = {
        "summary": str
    }
