from pydantic import BaseModel


class AskRequest(BaseModel):
    user: str
    question: str


class AskResponse(BaseModel):
    answer: str
    source: str | None = None
