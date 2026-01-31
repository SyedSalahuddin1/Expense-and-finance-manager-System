from repositories.account_repository_base import AccountRepositoryBase

class AccountRepository(AccountRepositoryBase):
    def __init__(self):
        self._accounts = {}
    
    def add(self, account):
        self._accounts[account.id] = account
    
    def get_by_id(self, account_id):
        account = self._accounts.get(account_id)
        
        if not account:
            raise ValueError(f"Account {account_id} not")
        return account
    
    def list_all(self):
        return list(self._accounts.values())
    
    