'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-10-09
Purpose: Input/Output description for Chat Bot Service
-----------------------------------------------------
'''
from .service_io import ServiceIO
from ..constants import ServiceString


class ChatBotIO(ServiceIO):
    service = ServiceString.CHAT_BOT
    required_input_fields = ["message","chatbot_id","user_id","mode","bot_document_ids"]
    optional_input_fields = ["context_document_ids"]
    input_structure = {
        "message": str, 
        "chatbot_id": str, 
        "user_id": str, 
        "mode": str, 
        "bot_document_ids": list, 
        "context_document_ids": list
    }

    output_structure = {
        "response": str,
        "session_name": str,
        "messages": list,
        "context": str
    }

