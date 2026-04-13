import pytest
from unittest.mock import Mock

from src.hotel_service import HotelService


def make_service():
    room_repository = Mock()
    guest_repository = Mock()
    stay_repository = Mock()
    waitlist_repository = Mock()
    service = HotelService(
        room_repository,
        guest_repository,
        stay_repository,
        waitlist_repository,
    )
    return service, room_repository, guest_repository, stay_repository, waitlist_repository


def test_check_in_raises_when_parameters_are_missing():
    service, *_ = make_service()

    with pytest.raises(ValueError, match="Guest ID and room ID are required"):
        service.check_in(None, 101)


def test_check_in_returns_false_when_guest_does_not_exist():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    guest_repository.exists.return_value = False

    result = service.check_in(999, 101)

    assert result is False


def test_check_in_marks_room_unavailable_on_success():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    guest_repository.exists.return_value = True
    room_repository.exists.return_value = True
    guest_repository.is_blocked.return_value = False
    guest_repository.has_pending_debt.return_value = False
    room_repository.is_available.return_value = True
    stay_repository.count_active_stays.return_value = 0
    waitlist_repository.next_guest.return_value = None
    waitlist_repository.has_entry.return_value = False

    result = service.check_in(1, 101)

    assert result is True
    room_repository.mark_unavailable.assert_called_once_with(101)
    stay_repository.create_stay.assert_called_once_with(1, 101)


def test_check_out_returns_false_when_stay_does_not_exist():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    stay_repository.is_room_with_guest.return_value = False

    result = service.check_out(1, 101)

    assert result is False


def test_join_waitlist_adds_entry_when_possible():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    guest_repository.exists.return_value = True
    room_repository.exists.return_value = True
    guest_repository.is_blocked.return_value = False
    guest_repository.has_pending_debt.return_value = False
    room_repository.is_available.return_value = False
    waitlist_repository.has_entry.return_value = False
    stay_repository.is_room_with_guest.return_value = False

    result = service.join_waitlist(4, 102)

    assert result is True
    waitlist_repository.add_entry.assert_called_once_with(4, 102)


def test_join_waitlist_raises_when_parameters_are_missing():
    service, *_ = make_service()

    with pytest.raises(ValueError, match="Guest ID and room ID are required"):
        service.join_waitlist(1, None)
