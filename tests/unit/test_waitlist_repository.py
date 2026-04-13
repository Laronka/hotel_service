import pytest

from src.waitlist_repository import WaitlistRepository


def test_add_entry_creates_waitlist_entry():
    repository = WaitlistRepository()

    repository.add_entry(4, 102)

    assert repository.has_entry(4, 102) is True


def test_has_any_entry_returns_true_when_room_has_waitlist():
    repository = WaitlistRepository()
    repository.add_entry(4, 102)

    assert repository.has_any_entry(102) is True


def test_next_guest_returns_first_guest_in_queue():
    repository = WaitlistRepository()
    repository.add_entry(4, 102)
    repository.add_entry(1, 102)

    assert repository.next_guest(102) == 4


def test_remove_entry_removes_waitlist_entry():
    repository = WaitlistRepository()
    repository.add_entry(4, 102)

    repository.remove_entry(4, 102)

    assert repository.has_entry(4, 102) is False


def test_remove_entry_raises_for_unknown_entry():
    repository = WaitlistRepository()

    with pytest.raises(ValueError, match="Waitlist entry not found"):
        repository.remove_entry(4, 102)
