from typing import Dict, List
from domain.account import Account
from repositories.account_repository_base import AccountRepositoryBase


class AccountRepository(AccountRepositoryBase):

    def __init__(self):
        self._accounts: Dict[int, Account] = {}

    def add(self, account: Account) -> None:
        if account.id in self._accounts:
            raise ValueError(f"Account with id {account.id} already exists")
        self._accounts[account.id] = account

    def get_by_id(self, account_id: int) -> Account:
        if account_id not in self._accounts:
            raise KeyError(f"Account with id {account_id} not found")
        return self._accounts[account_id]

    def list_all(self) -> List[Account]:
        return list(self._accounts.values())
