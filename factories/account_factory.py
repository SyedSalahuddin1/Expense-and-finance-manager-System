from domain.savings_account import SavingsAccount
from domain.credit_account import Credit_Account

class AccountFactory:
    def create(self, kind, **kwargs):
        if kind == "savings":
            return SavingsAccount(**kwargs)
        if kind == "credit":
            return Credit_Account(**kwargs)
        raise ValueError("Unknown account type")
    