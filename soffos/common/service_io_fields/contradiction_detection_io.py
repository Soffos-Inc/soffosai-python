from .service_io import ServiceIO
from ..constants import Services


class ContradictionDetectionIO(ServiceIO):
    service = Services.CONTRADICTION_DETECTION
    required_input_fields = ["text"]
    optional_input_fields = []
    input_structure = {
         "text": str
    }
    output_fields = ["contradictions"]
    output_structure = {
        "contradictions": [
            {
                "contradiction": str,
                "sentences": [
                    {
                        "text": str,
                        "span_start": int,
                        "span_end": int
                    },
                ]
            },
        ]
    }
