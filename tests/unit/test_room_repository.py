import pytest

from src.room_repository import RoomRepository


def test_exists_returns_true_for_existing_room():
    repository = RoomRepository()
    assert repository.exists(101) is True


def test_is_available_returns_false_for_unknown_room():
    repository = RoomRepository()
    assert repository.is_available(999) is False


def test_mark_unavailable_changes_room_state():
    repository = RoomRepository()

    repository.mark_unavailable(101)

    assert repository.is_available(101) is False


def test_mark_available_changes_room_state():
    repository = RoomRepository()

    repository.mark_available(102)

    assert repository.is_available(102) is True


def test_mark_unavailable_raises_for_unknown_room():
    repository = RoomRepository()

    with pytest.raises(ValueError, match="Room not found"):
        repository.mark_unavailable(999)
