from pydantic import BaseModel


class StartRequest(BaseModel):
    telegram_id: int
    username: str | None = None
    first_name: str
    last_name: str | None = None


class StartResponse(BaseModel):
    id: int
    telegram_id: int
    status: str | None
    created: bool
    is_admin: bool
