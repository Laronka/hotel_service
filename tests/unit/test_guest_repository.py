from src.guest_repository import GuestRepository


def test_exists_returns_true_for_existing_guest():
    repository = GuestRepository()
    assert repository.exists(1) is True


def test_is_blocked_returns_true_for_blocked_guest():
    repository = GuestRepository()
    assert repository.is_blocked(2) is True


def test_has_pending_debt_returns_true_when_guest_has_debt():
    repository = GuestRepository()
    assert repository.has_pending_debt(3) is True


def test_unknown_guest_is_not_blocked():
    repository = GuestRepository()
    assert repository.is_blocked(999) is False
