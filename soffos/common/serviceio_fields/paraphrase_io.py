from .service_io import ServiceIO
from ..constants import Services


class ParaphraseIO(ServiceIO):
    service = Services.PARAPHRASE
    required_input_fields = ["text"]
    input_structure = {
        "text": str
    }
    output_structure = {
        "paraphrase": str
    }
