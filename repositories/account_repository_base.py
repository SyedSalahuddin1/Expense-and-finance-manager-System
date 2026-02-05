from abc import ABC, abstractmethod
from typing import List 
from domain.account import Account

class AccountRepositoryBase(ABC):
    """
    Abstract repository interface for accessing Account entities.
    Acts as a boundary between application services and persistence.
    """

    @abstractmethod
    def add(self, account) -> None:
        """
        Adds an account to the repository.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, account_id) -> Account:
        """
        Retrieves an account by its identity.
        Raises an error if not found.
        """
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[Account]:
        """
        Returns all stored accounts.
        """
        raise NotImplementedError
