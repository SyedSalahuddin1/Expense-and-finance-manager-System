class Expense:
    def __init__(self, money, strategy):
        self._money = money
        self._strategy = strategy
    
    def apply_to(self, account):
        self._strategy.apply(account, self._money)
        