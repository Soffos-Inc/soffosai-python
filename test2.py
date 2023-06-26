import soffosai
from soffosai.core.pipeline import SoffosPipeline
from soffosai.core.nodes import ServiceNode
from soffosai.common.constants import ServiceString

src = {
    "text": ""
}

pipeline = SoffosPipeline(
    stages=[
        ServiceNode(service=ServiceString.SUMMARIZATION, inputs=[{"text": "pipeline", "sent_length": "pipeline"}]),
        ServiceNode(service=ServiceString.PARAPHRASE, inputs=[{"text": {0: "summary"}}]),
        ServiceNode(service=ServiceString.NER, inputs=[{"text": "pipeline"}]),
        ServiceNode(service=ServiceString.TAG_GENERATION, inputs=[{"text": {1: "paraphrase"}, "types": ["topic", "domain"]}])
    ]
)

def endpoint(request):
    # data = {**request.json()}
    data = {
        "user": "someuser",
        ""
    }

    return pipeline(data)
