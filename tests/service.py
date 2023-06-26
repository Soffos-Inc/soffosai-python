import soffosai
from soffosai import *


service = AmbiguityDetectionService()
output = service(
    text = "I saw his duck.",
    sentence_overlap = False,
    sentence_split=1,
    user = "client_user_id"
)
print(output)

service = AnswerScoringService()
output = service(
    user = "client_user_id",
    context="Genetic evidence suggests that dogs descended directly from wolves (Canis) and that the now-extinct wolf lineages that produced dogs branched off from the line that produced modern living wolves sometime between 27,000 and 40,000 years ago. The timing and location of dog domestication is a matter of debate. There is strong genetic evidence, however, that the first domestication events occurred somewhere in northern Eurasia between 14,000 and 29,000 years ago.",
    question="How long ago did dogs first become domesticated?",
    user_answer="around 20,000 years ago.",
    answer="Between 14,000 and 29,000 years ago."
)
print(output)

service = ContradictionDetectionService()
output = service(
    user = "client_user_id",
    text = "The source noted that the Shaheen-2, with a range of 2400 km, has never been tested by Pakistan. Pakistan has said that it performed several tests of its 2300 km-range Shaheen-2 missile in September 2004."
)
print(output)
################################ There is also a general DocumentsService class ##############################################
service = DocumentsIngestService()
output = service(
    user = "client_user_id",
    document_name='dogs',
    text="Genetic evidence suggests that dogs descended directly from wolves (Canis) and that the now-extinct wolf lineages that produced dogs branched off from the line that produced modern living wolves sometime between 27,000 and 40,000 years ago. The timing and location of dog domestication is a matter of debate. There is strong genetic evidence, however, that the first domestication events occurred somewhere in northern Eurasia between 14,000 and 29,000 years ago.",
)
print(output)
document_id = '908b42d4ae8f4e8d821d8fe228f4e744'

service = DocumentsSearchService()
output = service(user = "client_user_id", document_ids=['908b42d4ae8f4e8d821d8fe228f4e744'])
print(output)

service = DocumentsDeleteService()
output = service(user="client_user_id", document_ids=['908b42d4ae8f4e8d821d8fe228f4e744'])
print(output)
############################# DOCUMENT SERVICE #############################3
service = DocumentsService()
output = service.ingest(
    user = "client_user_id",
    document_name='dogs',
    text="Genetic evidence suggests that dogs descended directly from wolves (Canis) and that the now-extinct wolf lineages that produced dogs branched off from the line that produced modern living wolves sometime between 27,000 and 40,000 years ago. The timing and location of dog domestication is a matter of debate. There is strong genetic evidence, however, that the first domestication events occurred somewhere in northern Eurasia between 14,000 and 29,000 years ago.",
)
print(output)

output = service.search(user="client_user_id", document_ids=['71c9b431cacb457db53681286d76c62c'])
print(output)

output = service.delete(user="client_user_id", document_ids=['71c9b431cacb457db53681286d76c62c'])
print(output)
###################################################################################

service = EmailAnalysisService()
output = service(
    user = "client_user_id",
    text="Dear John,\n\nI hope this email finds you well. I am writing to follow up on a few topics that we discussed in our last meeting on the 31st of March. There are a few updates and urgent matters that I would like to discuss with you.\n\nFirstly, I wanted to touch base on the progress of the project we discussed. As per our conversation, we had agreed on a tentative timeline to complete the project by June 15th. However, due to unforeseen circumstances, we are falling behind schedule. It is imperative that we discuss the current situation and come up with a plan to get back on track as soon as possible.\n\nSecondly, as you are aware, we had discussed the possibility of scheduling a meeting with Mary regarding the financials on the 10th of April. However, we have yet to confirm a date and time for this meeting. Given the importance of this matter, I would like to request that we schedule this meeting within the next two weeks.\n\nLastly, I would like to express my appreciation for your ongoing support and assistance in these matters. Your expertise and guidance have been invaluable, and I am confident that we will be able to overcome any challenges that come our way.\n\nGiven the urgency of these matters, I would greatly appreciate a prompt response to this email. Kind regards,\nPeter"
)
print(output)

service = FileConverterService()
output = service(user="client_user_id", file="matrix.pdf", normalize=1)
print(output)

service = LanguageDetectionService()
output = service("client_user_id", "φιλόσοφος, που θεωρείται ο ιδρυτής της Δυτικής φιλοσοφίας και")
print(output)

##################################### Lets Discuss ###############################################
service = LetsDiscussService()
output = service.create(
    user="client_user_id",
    context="The James Webb Space Telescope is the largest, most powerful space telescope ever built. It will allow scientists to look at what our universe was like about 200 million years after the Big Bang. The telescope will be able to capture images of some of the first galaxies ever formed. It will also be able to observe objects in our solar system from Mars outward, look inside dust clouds to see where new stars and planets are forming and examine the atmospheres of planets orbiting other stars."
)
print(output)
{'session_id': 'e544b3eebe2b448bb053852874f31acf'}

output = service(
    user = "client_user_id",
    session_id='e544b3eebe2b448bb053852874f31acf',
    query='What is the purpose of observing this?'
)
print(output)

output = service.retrieve_sessions(
    user = "client_user_id",
    return_messages = False
)
print(output)

output = service.delete(
    user = "client_user_id",
    session_ids = ['196337f376fa4c6c9f434e8403662d7e', '5aed9013ddf449a29e135d56edc630c0']
)
print(output)
##########################################################################################

service = LogicalErrorDetectionService()
output = service(
    user = "client_user_id",
    text = "Nobody has found evidence that UFOs don't exist, therefore they must exist. Many people are saying that voter fraud is real, therefore it must be real."
)
print(output)

service = MicrolessonService()
output = service(
    user = "client_user_id",
    content=[
        {
            "source": "Telescope.docx",
            "text": "The James Webb Space Telescope is the largest, most powerful space telescope ever built. It will allow scientists to look at what our universe was like about 200 million years after the Big Bang. The telescope will be able to capture images of some of the first galaxies ever formed. It will also be able to observe objects in our solar system from Mars outward, look inside dust clouds to see where new stars and planets are forming and examine the atmospheres of planets orbiting other stars."
        },
        {
            "source": "dogs.docx",
            "text": "Genetic evidence suggests that dogs descended directly from wolves (Canis) and that the now-extinct wolf lineages that produced dogs branched off from the line that produced modern living wolves sometime between 27,000 and 40,000 years ago. The timing and location of dog domestication is a matter of debate. There is strong genetic evidence, however, that the first domestication events occurred somewhere in northern Eurasia between 14,000 and 29,000 years ago.",
        }
    ]
)
print(output)
service.add_content(
    source = "Telescope.docx",
    text = "The James Webb Space Telescope is the largest, most powerful space telescope ever built. It will allow scientists to look at what our universe was like about 200 million years after the Big Bang. The telescope will be able to capture images of some of the first galaxies ever formed. It will also be able to observe objects in our solar system from Mars outward, look inside dust clouds to see where new stars and planets are forming and examine the atmospheres of planets orbiting other stars."
)
service.add_content(
    source = "dogs.docx",
    text = "Genetic evidence suggests that dogs descended directly from wolves (Canis) and that the now-extinct wolf lineages that produced dogs branched off from the line that produced modern living wolves sometime between 27,000 and 40,000 years ago. The timing and location of dog domestication is a matter of debate. There is strong genetic evidence, however, that the first domestication events occurred somewhere in northern Eurasia between 14,000 and 29,000 years ago.",
)
output = service(user="client_user_id")
print(output)

