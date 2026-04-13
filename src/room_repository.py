class RoomRepository:
    def __init__(self):
        self._rooms = {
            101: {"category": "standard", "available": True},
            102: {"category": "standard", "available": False},
            201: {"category": "suite", "available": True},
            202: {"category": "suite", "available": False},
        }

    def exists(self, room_id: int) -> bool:
        return room_id in self._rooms

    def is_available(self, room_id: int) -> bool:
        if room_id not in self._rooms:
            return False
        return self._rooms[room_id]["available"]

    def mark_unavailable(self, room_id: int) -> None:
        if room_id not in self._rooms:
            raise ValueError("Room not found")
        self._rooms[room_id]["available"] = False

    def mark_available(self, room_id: int) -> None:
        if room_id not in self._rooms:
            raise ValueError("Room not found")
        self._rooms[room_id]["available"] = True
