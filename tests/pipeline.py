import soffos
from soffos.core.pipeline import SoffosPipeline
from soffos.core.nodes import ServiceNode
from soffos.common.constants import ServiceString


src = {
    "user": "franco", 
    "file": "matrix.pdf",
    "name": "matrix"
}
file_converter_node = ServiceNode(
    service=ServiceString.FILE_CONVERTER,
    source={
        "file": (0, "file")
    }
)

document_ingest_node = ServiceNode(
    service=ServiceString.DOCUMENTS_INGEST,
    source={
        "name": (0, "name"),
        "text": (1, "text")
    }
)

question_answering_node = ServiceNode(
    service=ServiceString.QUESTION_ANSWERING,
    source={
        "document_ids": (2, "document_id"),
        "message": "Who is Neo?"
    }
)

my_pipe = SoffosPipeline(
    stages = [file_converter_node, document_ingest_node, question_answering_node],
    user = 'franco',
    source = src
)

print(my_pipe.run()[3])
