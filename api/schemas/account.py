from pydantic import BaseModel, Field, field_validator
from typing import Literal


class AccountResponseSchema(BaseModel):
    id: int
    owner_name: str
    balance: float
    currency: str
    type: str


class AccountCreateSchema(BaseModel):
    owner_name: str = Field(..., min_length=2)
    opening_balance: float = Field(..., ge=0)
    currency: str = Field(..., min_length=3, max_length=3)
    type: Literal["savings", "credit"]

    interest_rate: float | None = Field(default=None, ge=0)
    credit_limit: float | None = Field(default=None, ge=0)

    @field_validator("interest_rate")
    @classmethod
    def validate_interest_rate(cls, v, info):
        if info.data.get("type") == "savings" and v is None:
            raise ValueError("interest_rate is required for savings account")
        return v

    @field_validator("credit_limit")
    @classmethod
    def validate_credit_limit(cls, v, info):
        if info.data.get("type") == "credit" and v is None:
            raise ValueError("credit_limit is required for credit account")
        return v
