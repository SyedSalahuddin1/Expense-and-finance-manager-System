from fastapi import APIRouter, Depends, HTTPException
from api.schemas.expense import ExpenseRequestSchema, ExpenseResponseSchema
from api.dependencies import get_expense_service
from domain.money import Money
from domain.expense import Expense
from strategies.expense_strategy import NormalExpenseStrategy

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.post("/", response_model=ExpenseResponseSchema)
def apply_expense(
    request: ExpenseRequestSchema,
    expense_service=Depends(get_expense_service),
):
    try:
        money = Money(request.amount, request.currency)
        expense = Expense(money, NormalExpenseStrategy())

        account = expense_service.apply_expense(
            request.account_id,
            expense,
        )

    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

    return ExpenseResponseSchema(
        account_id=account.id,
        new_balance=account.balance.amount,     # ✅ FIX
        currency=account.balance.currency,      # ✅ FIX
    )
