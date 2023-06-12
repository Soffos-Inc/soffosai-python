from .service_io import ServiceIO
from ..constants import ServiceString


class TableGeneratorIO(ServiceIO):
    service = ServiceString.TABLE_GENERATOR
    required_input_fields = ["table_format", "text"]
    input_structure = {
        "table_format": str, # markdown or CSV
        "text": str
    }
    output_structure = {
    "tables": [
            {
                "title": str,
                "table": str,
                "note": str
            },
        ]
    }
