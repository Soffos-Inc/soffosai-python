import json
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
#############################################################################################
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

service = LetsDiscussCreateService()
output = service("client_user_id", "The James Webb Space Telescope is the largest, most powerful space telescope ever built. It will allow scientists to look at what our universe was like about 200 million years after the Big Bang. The telescope will be able to capture images of some of the first galaxies ever formed. It will also be able to observe objects in our solar system from Mars outward, look inside dust clouds to see where new stars and planets are forming and examine the atmospheres of planets orbiting other stars.")
print(output)
{'session_id': '26c05c97bc334e4c90d05bac98d12524'}
service = LetsDiscussService()
output = service(
    user = "client_user_id",
    session_id='26c05c97bc334e4c90d05bac98d12524',
    query='What is the purpose of observing this?'
)
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
######################################### NER ############################################
service = NamedEntityRecognitionService()
output = service(
    user = 'client_id',
    text = "Patient Name: John Smith\nDate of Admission: June 15, 2023\nMedical Record Number: 123456789\n\nChief Complaint:\nThe patient presents with severe abdominal pain and vomiting.\n\nHistory of Present Illness:\nMr. Smith, a 45-year-old male, reports the onset of abdominal pain two days ago. The pain is localized to the lower right quadrant and has been progressively worsening. He has experienced multiple episodes of non-bloody vomiting. No significant alleviating or exacerbating factors have been identified.\n\nPast Medical History:\nThe patient has a history of hypertension and type 2 diabetes mellitus. He underwent an appendectomy in his childhood. He denies any known allergies or previous surgeries.\n\nMedications:\n- Lisinopril 10mg once daily for hypertension\n- Metformin 500mg twice daily for diabetes\n\nFamily History:\nThe patient's father had a history of myocardial infarction at the age of 60. His mother is alive and well with no significant medical conditions. There is no known family history of gastrointestinal disorders.\n\nSocial History:\nMr. Smith is a non-smoker and does not consume alcohol. He is married and works as an accountant. He denies any illicit drug use.\n\nPhysical Examination:\n- Vital Signs: Blood pressure 130/80 mmHg, heart rate 82 bpm, respiratory rate 16 breaths per minute, temperature 37.2°C (oral)\n- General: The patient appears uncomfortable and is lying still in bed.\n- Abdomen: There is tenderness in the right lower quadrant with guarding and rebound tenderness. No palpable masses or organomegaly. Bowel sounds are diminished.\n\nAssessment and Plan:\nThe patient's presentation is concerning for acute appendicitis. He will undergo further diagnostic evaluation, including complete blood count, urinalysis, and abdominal ultrasound. In the meantime, he will be kept NPO (nothing by mouth) and started on intravenous fluids. Surgical consultation will be obtained for potential appendectomy.\n\nPlease note that this is a fictional clinical text generated for demonstration purposes only. Any resemblance to actual patients or medical scenarios is purely coincidental.",
    labels = {
        "PERSON": "Refers to the name of the patient",
        "DATE": "Represents dates mentioned in the text",
        "MEDICAL_RECORD_NUMBER": "Identifies the unique identifier for the patient's medical record",
        "CHIEF_COMPLAINT": "Describes the primary reason for the patient's visit or main symptom",
        "SURGICAL_HISTORY": "Lists any previous surgeries the patient has undergone.",
        "ALLERGIES": "Indicates any known allergies or sensitivities the patient has",
        "MEDICATION": "Refers to current medications being taken by the patient",
        "DIAGNOSIS": "Specifies the preliminary or final diagnosis of the patient's condition"
    }
)
print(output)
service.add_label("PERSON", "Refers to the name of the patient")
service.add_label("DATE", "Represents dates mentioned in the text")
output = service(
    user = 'client_id',
    text = "Patient Name: John Smith\nDate of Admission: June 15, 2023\nMedical Record Number: 123456789\n\nChief Complaint:\nThe patient presents with severe abdominal pain and vomiting.\n\nHistory of Present Illness:\nMr. Smith, a 45-year-old male, reports the onset of abdominal pain two days ago. The pain is localized to the lower right quadrant and has been progressively worsening. He has experienced multiple episodes of non-bloody vomiting. No significant alleviating or exacerbating factors have been identified.\n\nPast Medical History:\nThe patient has a history of hypertension and type 2 diabetes mellitus. He underwent an appendectomy in his childhood. He denies any known allergies or previous surgeries.\n\nMedications:\n- Lisinopril 10mg once daily for hypertension\n- Metformin 500mg twice daily for diabetes\n\nFamily History:\nThe patient's father had a history of myocardial infarction at the age of 60. His mother is alive and well with no significant medical conditions. There is no known family history of gastrointestinal disorders.\n\nSocial History:\nMr. Smith is a non-smoker and does not consume alcohol. He is married and works as an accountant. He denies any illicit drug use.\n\nPhysical Examination:\n- Vital Signs: Blood pressure 130/80 mmHg, heart rate 82 bpm, respiratory rate 16 breaths per minute, temperature 37.2°C (oral)\n- General: The patient appears uncomfortable and is lying still in bed.\n- Abdomen: There is tenderness in the right lower quadrant with guarding and rebound tenderness. No palpable masses or organomegaly. Bowel sounds are diminished.\n\nAssessment and Plan:\nThe patient's presentation is concerning for acute appendicitis. He will undergo further diagnostic evaluation, including complete blood count, urinalysis, and abdominal ultrasound. In the meantime, he will be kept NPO (nothing by mouth) and started on intravenous fluids. Surgical consultation will be obtained for potential appendectomy.\n\nPlease note that this is a fictional clinical text generated for demonstration purposes only. Any resemblance to actual patients or medical scenarios is purely coincidental.",
)
print(output)
###############################################################################

service = ParaphraseService()
output = service(
    user = "client_id", 
    text = "During mitosis, a cell duplicates all of its contents, including its chromosomes, and splits to form two identical daughter cells. Because this process is so critical, the steps of mitosis are carefully controlled by certain genes. When mitosis is not regulated correctly, health problems such as cancer can result."
)
print(output)

service = SimplifyService()
output = service(
    user = "client_id", 
    text = "During mitosis, a cell duplicates all of its contents, including its chromosomes, and splits to form two identical daughter cells. Because this process is so critical, the steps of mitosis are carefully controlled by certain genes. When mitosis is not regulated correctly, health problems such as cancer can result."
)
print(output)

service = ProfanityService()
output = service(
    user = "client_id",
    text = "Your look like shit on your shirt! Fucking go home and change."
)
print(output)

service = QuestionAndAnswerGenerationService()
output = service(
    user = "client_id",
    text = "AI and specifically NLP is a very powerful component to any application that makes it powerful, interesting and creative. However, implementing the NLP components can sometimes be hard, or very costly in cases where an NLP engineering team has to be hired to build it. Especially, since NLP keeps evolving at an absurd rate, it might be impossible for a developer to keep up with the advancements in terms of work that needs to be done or money that need to be spent to keep their NLP at a state where it can compete with similar apps out there. Here at Soffos we have packaged several high-level functionalities as modules, some of which require multiple types of NLP and complex logic, for developers to use out-of-the-box, as is, removing the need to develop it themselves. Moreover, Soffos continuously updates their modules to match the state of the art. Developers will never need to maintain any AI/NLP related component of their application. All they need is to be creative, come up with ideas, and combine our modules however they desire to come up with amazing intelligent applications.",
    sentence_overlap = True,
    sentence_split = 5
)
print(json.dumps(output, indent=4))

service = QuestionAnsweringService()
output = service(
    user = "client_id",
    question = "What is the topic?",
    document_text = "The James Webb Space Telescope is the largest, most powerful space telescope ever built. It will allow scientists to look at what our universe was like about 200 million years after the Big Bang. The telescope will be able to capture images of some of the first galaxies ever formed. It will also be able to observe objects in our solar system from Mars outward, look inside dust clouds to see where new stars and planets are forming and examine the atmospheres of planets orbiting other stars.",
)
print(json.dumps(output, indent=4))

service = ReviewTaggerService()
output = service(
    user = "client_id",
    text = "This oven has been a complete disaster from the start. After about 2 weeks of use, the oven and broiler burners would turn off suddenly after being on for only 5 seconds. This has been an ongoing issue for months, and it still does not work."
)
print(json.dumps(output, indent=4))

service = SentimentAnalysisService()
output = service(
    user = "client_id",
    text = "Avocado shake tastes great!"
)
print(json.dumps(output, indent=4))

service = SummarizationService()
output = service(
    user = "client_id",
    text = "Ludwig van Beethoven (baptised 17 December 1770 – 26 March 1827) was a German composer and pianist. ... After some months of bedridden illness, he died in 1827. Beethoven's works remain mainstays of the classical music repertoire.",
    sent_length=2
)
print(json.dumps(output, indent=4))

service = TableGeneratorService()
output = service(
    user = "client_id",
    text = "Demographic and socioeconomic factors can contribute to community spread of COVID-19. The aim of this study is to describe the demographics and socioeconomic factors in relation to geolocation of COVID-19 patients who were discharged from the emergency department (ED) back into the community...",
    table_format = 'markdown'
)
print(json.dumps(output, indent=4))

service = TagGenerationService()
output = service(
    user = "client_id",
    text = "The Matrix is a 1999 science fiction action film written and directed by the Wachowskis. It is the first installment in The Matrix film series...",
    n = 3
)
print(json.dumps(output, indent=4))

service = TranscriptCorrectionService()
output = service(
    user = "client_id",
    text = " We just want to show people or services can't help them. Create amazing. Applications"
)
print(json.dumps(output, indent=4))
