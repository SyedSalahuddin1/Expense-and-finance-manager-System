from repositories.account_repository import AccountRepository
from factories.account_factory import AccountFactory
from domain.money import Money

_account_repository = AccountRepository()
_account_factory = AccountFactory()


def _init_accounts():
    if not _account_repository.list_all():
        acc = _account_factory.create(
            kind="savings",
            account_id=1,
            owner_name="Salahuddin",
            opening_balance=Money(1000, "USD"),
            interest_rate=0.05,
        )
        _account_repository.add(acc)


_init_accounts()


def get_account_repository():
    return _account_repository


def get_account_factory():
    return _account_factory
