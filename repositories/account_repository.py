from repositories.account_repository_base import AccountRepositoryBase


class AccountRepository(AccountRepositoryBase):
    """
    In-memory implementation of AccountRepositoryBase.
    """

    def __init__(self):
        self._accounts = {}

    def add(self, account) -> None:
        if not hasattr(account, "id"):
            raise TypeError("Account must have an id")

        if account.id in self._accounts:
            raise ValueError(f"Account with id {account.id} already exists")

        self._accounts[account.id] = account

    def get_by_id(self, account_id):
        if account_id not in self._accounts:
            raise KeyError(f"Account with id {account_id} not found")

        return self._accounts[account_id]

    def list_all(self):
        # Return a copy to protect internal state
        return list(self._accounts.values())
