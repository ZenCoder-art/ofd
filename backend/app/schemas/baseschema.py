from typing import Any, Optional

from pydantic import BaseModel


class SuccessResponseSchema(BaseModel):
    code: int = 200
    message: str = "Success"
    data: Optional[Any] = None

    class Config:
        json_schema_extra = {
            "example": {"code": 200, "message": "success", "data:": dict()}
        }


class ErrorResponseSchema(BaseModel):
    code: int = 400
    message: str = "Error"
    loc: Optional[str] = None
