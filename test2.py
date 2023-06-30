import soffosai
from soffosai.core.pipelines import Pipeline
from soffosai.core.nodes import NodeConfig
from soffosai.common.constants import ServiceString

src = {
    "text": ""
}

pipeline = Pipeline(
    stages=[
        NodeConfig(service=ServiceString.SUMMARIZATION, inputs=[{"text": "pipeline", "sent_length": "pipeline"}]),
        NodeConfig(service=ServiceString.PARAPHRASE, inputs=[{"text": {0: "summary"}}]),
        NodeConfig(service=ServiceString.NER, inputs=[{"text": "pipeline"}]),
        NodeConfig(service=ServiceString.TAG_GENERATION, inputs=[{"text": {1: "paraphrase"}, "types": ["topic", "domain"]}])
    ]
)

def endpoint(request):
    # data = {**request.json()}
    data = {
        "user": "someuser",
        ""
    }

    return pipeline(data)
