from soffos import Client, Services, SoffosAiResponse
from tagged import tagged_elements

api_key = "Token a1739a8f-c2cf-45e0-9bb1-0fd88beb717d"

documents_client = Client(apikey=api_key)

documents_client.service = Services.DOCUMENTS_INGEST
documents_client.user = "me"
documents_client.src = {
    "name": "ddd"
}
documents_client.tagged_elements = tagged_elements
response = documents_client.get_response()
print(response.raw_response)
