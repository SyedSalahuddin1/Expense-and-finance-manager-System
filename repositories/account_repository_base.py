from abc import ABC, abstractmethod

class AccountRepositoryBase(ABC):
    def add(self, account):
        pass
    
    @abstractmethod
    def get_by_id(self, account_id):
        pass
    
    @abstractmethod
    def list_all(self):
        pass
    