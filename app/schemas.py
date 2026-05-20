from typing import Optional

from pydantic import BaseModel, Field


class UserQuery(BaseModel):
    text: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="The incoming raw text prompt to check",
    )
    user_id: str = Field(
        ..., description="Unique identification string of the client user"
    )


class GuardrailResponse(BaseModel):
    is_safe: bool = Field(..., description="Flags if the text passed safety protocols")
    risk_score: float = Field(
        ..., description="Calculated metric from 0.0 (safe) to 1.0 (highly volatile)"
    )
    cleaned_text: str = Field(..., description="Sanitized version of user text")
    detected_violation: Optional[str] = Field(
        None, description="Type of threat vector flagged if any"
    )
