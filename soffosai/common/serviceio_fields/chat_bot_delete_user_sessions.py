'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Updated at: 2023-11-08
Purpose: Input/Output description for Chat Bot Delete User Sessions Service
-----------------------------------------------------
'''
from .service_io import ServiceIO
from ..constants import ServiceString


class ChatBotDeleteUserSessionsIO(ServiceIO):
    service = ServiceString.CHAT_BOT_DELETE_USER_SESSIONS
    required_input_fields = ["chatbot_id","user_id"]
    optional_input_fields = ["session_ids"]
    input_structure = {
        "chatbot_id": str, 
        "user_id": str, 
        "session_ids": list
    }

    output_structure = {
        "success": bool
    }

