'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2024-03-03
Purpose: Input/Output description for Chat Bots Delete Service
-----------------------------------------------------
'''
from .service_io import ServiceIO
from ..constants import ServiceString


class ChatBotsDeleteIO(ServiceIO):
    service = ServiceString.CHAT_BOTS_DELETE
    required_input_fields = ["chatbot_ids"]
    optional_input_fields = ["engine"]
    input_structure = {
        "engine": str, 
        "chatbot_ids": list
    }

    output_structure = {
        "engine": str,
        "success": bool
    }

