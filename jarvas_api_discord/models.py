from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    msg: str


class ChannelMessage(BaseModel):
    name: str
    message: str
    id_channel: int
