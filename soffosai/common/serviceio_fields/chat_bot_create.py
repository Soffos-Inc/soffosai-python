'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-11-08
Purpose: Input/Output description for Chat Bot Create Service
-----------------------------------------------------
'''
from .service_io import ServiceIO
from ..constants import ServiceString


class ChatBotCreateIO(ServiceIO):
    service = ServiceString.CHAT_BOT_CREATE
    required_input_fields = ["role","document_name"]
    optional_input_fields = ["chatbot_id"]
    input_structure = {
        "role": str, 
        "document_name": str, 
        "chatbot_id": str
    }

    output_structure = {
        "chatbot_id": str,
        "success": bool
    }

