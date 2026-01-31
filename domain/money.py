class Money:
    """
    Value Object representing money.
    Immutable and compared by value.
    """

    def __init__(self, amount: float, currency: str):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")

        if amount < 0:
            raise ValueError("Amount cannot be negative")

        if not currency or not isinstance(currency, str):
            raise ValueError("Currency must be a non-empty string")

        self._amount = float(amount)
        self._currency = currency.upper()

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def currency(self) -> str:
        return self._currency

    def _assert_same_currency(self, other: "Money"):
        if not isinstance(other, Money):
            raise TypeError("Operation requires Money instance")

        if self.currency != other.currency:
            raise ValueError("Currency mismatch")

    def add(self, other: "Money") -> "Money":
        self._assert_same_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def subtract(self, other: "Money") -> "Money":
        self._assert_same_currency(other)

        if self.amount < other.amount:
            raise ValueError("Insufficient amount")

        return Money(self.amount - other.amount, self.currency)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def __repr__(self) -> str:
        return f"Money(amount={self.amount}, currency='{self.currency}')"
