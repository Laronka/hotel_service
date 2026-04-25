import pytest

from src.hotel_service import HotelService
from src.guest_repository import GuestRepository
from src.room_repository import RoomRepository
from src.stay_repository import StayRepository
from src.waitlist_repository import WaitlistRepository

""" 
Criada função make service onde está sendo instanciado os repositórios que serão utilizados nos testes.
"""
def make_service():
    room_repository = RoomRepository()
    guest_repository = GuestRepository()
    stay_repository = StayRepository()
    waitlist_repository = WaitlistRepository()
    service = HotelService(
        room_repository,
        guest_repository,
        stay_repository,
        waitlist_repository,
    )
    return service, room_repository, guest_repository, stay_repository, waitlist_repository

def test_check_in_com_sucesso():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    test = service.check_in(1, 101)

    assert test is True
    assert room_repository.is_available(101) is False
    assert stay_repository.has_active_stay(101) is True

