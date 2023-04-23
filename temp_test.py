# from soffos.common.serviceio_fields import DocumentSearchIO
# from soffos.common.serviceio_fields import AmbiguityDetectionIO
# from soffos.pipeline import SoffosPipeline
# from soffos import Services
# a = DocumentSearchIO()
# print(a.output_fields)

# print(isinstance(str,type))
# my_pipe = SoffosPipeline([Services.AMBIGUITY_DETECTION, Services.CONTRADICTION_DETECTION])
from soffos import Services
from soffos.common.service_io_map import SERVICE_IO_MAP


print(SERVICE_IO_MAP[Services.EMOTION_DETECTION].required_input_fields)
