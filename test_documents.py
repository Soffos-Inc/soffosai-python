from soffos import Client, Services, SoffosAiResponse
from tagged import tagged_elements
from apikey import api_key


documents_client = Client(apikey=api_key)

documents_client.service = Services.DOCUMENTS_INGEST
documents_client.user = "me"
documents_client.src = {
    "name": "ddd"
}
documents_client.tagged_elements = tagged_elements
response = documents_client.get_response()
print(response.raw_response)
