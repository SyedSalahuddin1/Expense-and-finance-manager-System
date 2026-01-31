class ExpenseStrategy:
    def apply(self, account, money):
        raise NotImplementedError
    
class NormalExpense(ExpenseStrategy):
    def apply(self, account, money):
        account.withdraw(money)
        
class TaxedExpense(ExpenseStrategy):
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate 
        
    def apply(self, account, money):
        tax = money.amount * self.tax_rate
        total = money.amount + tax 
        
        from domain.money import Money
        account.withdraw(Money(total, money.currency))
        