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

""" 
Função que testa o checkin com sucesso.
"""
def test_check_in_com_sucesso():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    test = service.check_in(1, 101)

    assert test is True
    assert room_repository.is_available(101) is False
    assert stay_repository.has_active_stay(101) is True

""" 
Função que verifica a tentativa de checkin em um quarto inexistente, deve retornar falso para um room id inexistente.
"""
def test_check_in_quarto_inexistente():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    quarto = service.check_in(1, 999)

    assert quarto is False

""" 
Função que verifica a tentativa de checkin de um hospede inexistente.
"""
def test_check_in_hospede_inexistente():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    hospede = service.check_in(999, 101)

    assert hospede is False

""" 
Função que verifica a tentativa de checkin de um hospede com debito pendente.
"""
def test_check_bloqueado_por_debito():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    bloqueado = service.check_in(3, 101)

    assert bloqueado is False

""" 
Função que verifica a tentativa de checkin de um hospede bloqueado.
"""
def test_check_in_bloqueado_por_usuario_bloqueado():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    bloqueado = service.check_in(2, 101)

    assert bloqueado is False

""" 
Função que verifica o check-in bloqueado após duas hospedagens.
"""
def test_check_in_bloqueado_por_mais_de_duas_hospedagens():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    checkin1 = service.check_in(1, 101)
    checkin2 = service.check_in(1, 201)
    room_repository.mark_available(102) 
    checkin3 = service.check_in(1, 102)

    assert checkin1 is True
    assert checkin2 is True
    assert checkin3 is False

""" 
Função que verifica o check-in bloqueado após duas hospedagens.
"""
def test_entra_em_fila_de_espera():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    fila = service.join_waitlist(4, 202)

    assert fila is True
    assert waitlist_repository.has_entry(4, 202) is True

"""
Função que testa a entrada duplica na fila de espera
"""           
def test_entrada_duplicada_fila_de_espera():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    fila1 = service.join_waitlist(4, 202)
    fila2 = service.join_waitlist(4, 202)

    assert fila1 is True
    assert fila2 is False

"""
Função que testa o check-out com sucesso
""" 
def test_check_out_com_sucesso():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    service.check_in(1, 101)
    checkout = service.check_out(1, 101)

    assert checkout is True
    assert room_repository.is_available(101) is True
    assert stay_repository.has_active_stay(101) is False

"""
Função que testa o check-out com fila de espera
""" 
def test_check_out_com_fila_de_espera():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    service.check_in(1, 101)
    service.join_waitlist(4, 101)
    service.check_out(1, 101)

    assert room_repository.is_available(101) is False
    
"""
Função que testa o check-in de um hospedena fila
"""
def test_check_in_com_sucesso_hospode_na_fila():
    service, room_repository, guest_repository, stay_repository, waitlist_repository = make_service()
    service.join_waitlist(4, 102)
    room_repository.mark_available(102)
    checkin = service.check_in(4, 102)

    assert checkin is True
    assert stay_repository.has_active_stay(102) is True
    assert waitlist_repository.has_entry(4, 102) is False

    