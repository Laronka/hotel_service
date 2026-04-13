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