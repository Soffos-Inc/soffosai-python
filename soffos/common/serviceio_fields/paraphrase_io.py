from .service_io import ServiceIO
from ..constants import ServiceString


class ParaphraseIO(ServiceIO):
    service = ServiceString.PARAPHRASE
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "paraphrase": str
    }
