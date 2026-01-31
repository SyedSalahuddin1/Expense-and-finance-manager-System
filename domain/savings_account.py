from domain.account import Account
from domain.money import Money

class SavingsAccount(Account):
    def __init__(self, account_id: int, owner_name: str, opening_balance: Money, interest_rate):
        super().__init__(account_id, owner_name, opening_balance)
        self._interest_rate = interest_rate
        
    def apply_interest(self):
        interest = Money(
            self._balance.amount * self._interest_rate,
            self.balance.currency
        )
        self.deposit(interest)
        