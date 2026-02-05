from pydantic import BaseModel, Field


class ExpenseRequestSchema(BaseModel):
    account_id: int = Field(..., gt=0)
    amount: float = Field(..., gt=0)
    currency: str = Field(..., min_length=3, max_length=3)


class ExpenseResponseSchema(BaseModel):
    account_id: int
    new_balance: float
    currency: str
