import pytest

from src.stay_repository import StayRepository


def test_create_stay_registers_active_stay():
    repository = StayRepository()

    repository.create_stay(1, 101)

    assert repository.has_active_stay(101) is True


def test_is_room_with_guest_returns_true_for_matching_stay():
    repository = StayRepository()
    repository.create_stay(1, 101)

    assert repository.is_room_with_guest(1, 101) is True


def test_count_active_stays_counts_only_given_guest():
    repository = StayRepository()
    repository.create_stay(1, 101)
    repository.create_stay(1, 201)
    repository.create_stay(4, 102)

    assert repository.count_active_stays(1) == 2


def test_close_stay_removes_active_stay():
    repository = StayRepository()
    repository.create_stay(1, 101)

    repository.close_stay(1, 101)

    assert repository.has_active_stay(101) is False


def test_close_stay_raises_for_missing_stay():
    repository = StayRepository()

    with pytest.raises(ValueError, match="Active stay not found"):
        repository.close_stay(1, 101)
