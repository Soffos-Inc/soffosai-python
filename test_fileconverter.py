from soffos.core.services import QuestionAnsweringService, SoffosAIService
from soffos.common.constants import ServiceString

src = {
    'user': "b5601df8-6af3-4c1a-9ded-b7df4c506eab",
    'file': 'Epidemiology.docx'
}
service = SoffosAIService(
    service = ServiceString.FILE_CONVERTER,
    user = src.get('user'),
    src = src
)

response = service.get_response()
print(response)


# print(response.raw_response)