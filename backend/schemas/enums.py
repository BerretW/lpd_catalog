from enum import Enum

class StatusEnum(str, Enum):
    OK = "OK"
    KE_KONTROLE = "ke kontrole"
    VYMENA = "na vymenu"