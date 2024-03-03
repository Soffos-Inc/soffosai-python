import json
import soffosai
from soffosai import SoffosAIServices

soffosai.api_key = "<your API key>"


service = SoffosAIServices.SummarizationService()
output = service(
    user = "client_id",
    text = "Ludwig van Beethoven (baptised 17 December 1770 – 26 March 1827) was a German composer and pianist. ... After some months of bedridden illness, he died in 1827. Beethoven's works remain mainstays of the classical music repertoire.",
    sent_length=2
)
print(json.dumps(output, indent=4))
