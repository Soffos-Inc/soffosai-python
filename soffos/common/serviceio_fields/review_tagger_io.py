from .service_io import ServiceIO
from ..constants import Services


class ReviewTaggerIO(ServiceIO):
    service = Services.REVIEW_TAGGER
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "object": str,
        "action": str,
        "fault": str
    }
