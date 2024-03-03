import soffosai
from soffosai import SoffosAIServices

soffosai.api_key = "<your API key>"

output1 = SoffosAIServices.DiscussCreateService.call(
    user="client_user_id",
    context="The James Webb Space Telescope is the largest, most powerful space telescope ever built. It will allow scientists to look at what our universe was like about 200 million years after the Big Bang. The telescope will be able to capture images of some of the first galaxies ever formed. It will also be able to observe objects in our solar system from Mars outward, look inside dust clouds to see where new stars and planets are forming and examine the atmospheres of planets orbiting other stars."
)
print(output1)

output2 = SoffosAIServices.DiscussQueryService.call(
    user = "client_user_id",
    session_id=output1.get("session_id"),
    query='What is the purpose of observing this?'
)
print(output2)

output3 = SoffosAIServices.DiscussCountService.call(
    user = "client_user_id",
    return_messages = False
)
print(output3)

output4 = SoffosAIServices.DiscussDeleteService.call(
    user = "client_user_id",
    session_ids = [output1.get("session_id")]
)
print(output4)