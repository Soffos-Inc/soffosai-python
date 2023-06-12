'''
Soffos Inc. Python SDK package
'''

from .client import SoffosAiResponse
from .common.constants import ServiceString
import os
import sys

api_key = os.environ.get("SOFFOSAI_API_KEY")

__all__ = [
    "api_key",
    "Client",
    "SoffosAiResponse",
    "Services"
]
