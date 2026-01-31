class AccountObserver:
    def notify(self, account, message):
        raise NotImplementedError


class ConsoleLogger(AccountObserver):
    def notify(self, account, message):
        print(f"[LOG] Account {account.id}: {message}")
