from .service_io import ServiceIO
from ..constants import ServiceString


class ReviewTaggerIO(ServiceIO):
    service = ServiceString.REVIEW_TAGGER
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "object": str,
        "action": str,
        "fault": str
    }
