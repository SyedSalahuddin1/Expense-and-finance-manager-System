from abc import ABC, abstractmethod


class AccountObserver(ABC):
    """
    Observer interface for reacting to account-related events.
    Observers must not affect domain behavior.
    """

    @abstractmethod
    def notify(self, account, message: str) -> None:
        """
        Receives notification about an account event.
        """
        raise NotImplementedError


class ConsoleAccountObserver(AccountObserver):
    """
    Simple observer that logs account events to the console.
    """

    def notify(self, account, message: str) -> None:
        print(f"[ACCOUNT {account.id}] {message}")
