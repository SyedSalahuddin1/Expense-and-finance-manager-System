from domain.account import Account
from domain.account import Money

class Credit_Account(Account):
    def __init__(self, account_id: int, owner_name: str, opening_balance: Money, credit_limit):
        super().__init__(account_id, owner_name, opening_balance)
        self._credit_limit = credit_limit 
        
    def withdraw(self, money: Money):
        new_balance_amount = self.balance.amount - money.amount
        
        if new_balance_amount < self._credit_limit:
            raise ValueError("Credit Limit Exceeded")
        
        self._balance = Money(new_balance_amount, self.balance.currency)
        