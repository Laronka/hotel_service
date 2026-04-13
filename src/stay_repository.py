class StayRepository:
    def __init__(self):
        self._active_stays = []

    def create_stay(self, guest_id: int, room_id: int) -> None:
        self._active_stays.append({"guest_id": guest_id, "room_id": room_id})

    def has_active_stay(self, room_id: int) -> bool:
        return any(stay["room_id"] == room_id for stay in self._active_stays)

    def is_room_with_guest(self, guest_id: int, room_id: int) -> bool:
        return any(
            stay["guest_id"] == guest_id and stay["room_id"] == room_id
            for stay in self._active_stays
        )

    def count_active_stays(self, guest_id: int) -> int:
        return sum(1 for stay in self._active_stays if stay["guest_id"] == guest_id)

    def close_stay(self, guest_id: int, room_id: int) -> None:
        for index, stay in enumerate(self._active_stays):
            if stay["guest_id"] == guest_id and stay["room_id"] == room_id:
                del self._active_stays[index]
                return
        raise ValueError("Active stay not found")
