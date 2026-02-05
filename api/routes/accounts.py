from fastapi import APIRouter, Depends, HTTPException
from domain.money import Money
from api.schemas.account import AccountResponseSchema, AccountCreateSchema
from api.dependencies import (
    get_account_repository,
    get_account_factory,
)

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.get("/", response_model=list[AccountResponseSchema])
def list_accounts(
    repository=Depends(get_account_repository),
):
    accounts = repository.list_all()

    return [
        AccountResponseSchema(
            id=acc.id,
            owner_name=acc.owner_name,
            balance=acc.balance.amount,        
            currency=acc.balance.currency,     
            type=acc.__class__.__name__.replace("Account", "").lower(),
        )
        for acc in accounts
    ]


@router.get("/{account_id}", response_model=AccountResponseSchema)
def get_account(
    account_id: int,
    repository=Depends(get_account_repository),
):
    try:
        acc = repository.get_by_id(account_id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return AccountResponseSchema(
        id=acc.id,
        owner_name=acc.owner_name,
        balance=acc.balance.amount,            
        currency=acc.balance.currency,         
        type=acc.__class__.__name__.replace("Account", "").lower(),
    )


@router.post("/", response_model=AccountResponseSchema, status_code=201)
def create_account(
    request: AccountCreateSchema,
    repository=Depends(get_account_repository),
    factory=Depends(get_account_factory),
):
    try:
        account = factory.create(
            kind=request.type,
            account_id=len(repository.list_all()) + 1,
            owner_name=request.owner_name,
            opening_balance=Money(
                request.opening_balance,
                request.currency,
            ),
            interest_rate=request.interest_rate,
            credit_limit=request.credit_limit,
        )
        repository.add(account)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return AccountResponseSchema(
        id=account.id,
        owner_name=account.owner_name,
        balance=account.balance.amount,        
        currency=account.balance.currency,     
        type=request.type,
    )
