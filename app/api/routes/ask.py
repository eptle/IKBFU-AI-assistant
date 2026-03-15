from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AskRequest(BaseModel):
    user_id: int
    question: str

class AskResponse(BaseModel):
    answer: str

@router.post("/", response_model=AskResponse)
async def ask(req: AskRequest):
    # Заглушка
    return AskResponse(answer=f"Эхо: {req.question}")