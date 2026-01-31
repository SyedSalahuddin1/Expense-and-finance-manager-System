class Money:
    def __init__(self, amount: float, currency: str):
        if amount < 0:
            raise ValueError("Money Can't be negative!")
        
        if not currency:
            raise ValueError("Currency Can't be empty!")
        
        self._amount = amount
        self._currency = currency
        
    @property
    def amount(self):
        return self._amount
    
    @property
    def currency(self):
        return self._currency
    
    def add(self, other):
        if self.currency != other.currency:
            raise ValueError("Currency Mismatch")
        return Money(self.amount + other.amount, self.currency)
    
    def subtract(self, other):
        if self.currency != other.currency:
            raise ValueError("Currency Mismatch")
        if self.amount < other.amount:
            raise ValueError("Insufficient balance")
        return Money(self.amount - other.amount, self.currency)
    
    def __repr__(self):
        return f"Money({self._amount}, '{self._currency}')"
    