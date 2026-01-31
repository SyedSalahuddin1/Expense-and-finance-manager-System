from domain.money import Money

class Account:
    def __init__(self, account_id: int, owner_name: str, opening_balance: Money):
        if opening_balance.amount < 0:
            raise ValueError("Opening balance cannot be negative")
        
        self._account_id = account_id
        self._owner_name = owner_name 
        self._balance = opening_balance    
        self._observers = []
    
    @property
    def account_id(self):
        return self._account_id
    
    @property
    def owner_name(self):
        return self._owner_name
    
    @property
    def balance(self):
        return self._balance
    
    def _notify(self, message):
        for obs in self._observers:
            obs.notify(self, message)
            
    def add_observer(self, observer):
        self._observers.append(observer)
    
    def deposit(self, money: Money):
        self._balance = self._balance.add(money)
        self._notify(f"Deposited {money}")

    
    def withdraw(self, money:Money):
        self._balance = self._balance.subtract(money)
        self._notify(f"Withdraw {money}")
                
    def __repr__(self):
        return f"Account(account_id={self._account_id}, owner_name='{self._owner_name}', balance={self._balance})"
    