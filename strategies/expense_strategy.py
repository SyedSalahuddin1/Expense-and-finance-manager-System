from locale import currency
from domain.money import Money

class ExpenseStrategy:
    def apply(self, account, money):
        raise NotImplementedError

class NormalExpense(ExpenseStrategy):
    def apply(self, account, money):
        account.withdraw(money)
        
class TaxedExpense(ExpenseStrategy):
    def __init__(self, tax_rate):
        self._tax_rate = tax_rate
        
    def apply(self, account, money):
        tax = money.account * self._tax_rate
        total = money.amount + tax 
        
        account.withdraw(Money(total, money.currency))
        