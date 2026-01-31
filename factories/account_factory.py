from domain.savings_account import SavingsAccount
from domain.credit_account import CreditAccount


class AccountFactory:
    """
    Factory responsible for creating Account objects.
    Centralizes knowledge of account types.
    """

    _ACCOUNT_TYPES = {
        "savings": SavingsAccount,
        "credit": CreditAccount,
    }

    def create(self, kind: str, **kwargs):
        if kind not in self._ACCOUNT_TYPES:
            raise ValueError(
                f"Unsupported account type '{kind}'. "
                f"Supported types: {list(self._ACCOUNT_TYPES.keys())}"
            )

        account_class = self._ACCOUNT_TYPES[kind]
        return account_class(**kwargs)
