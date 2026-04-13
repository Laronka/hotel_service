class WaitlistRepository:
    def __init__(self):
        self._entries = []

    def add_entry(self, guest_id: int, room_id: int) -> None:
        self._entries.append({"guest_id": guest_id, "room_id": room_id})

    def has_entry(self, guest_id: int, room_id: int) -> bool:
        return any(
            entry["guest_id"] == guest_id and entry["room_id"] == room_id
            for entry in self._entries
        )

    def has_any_entry(self, room_id: int) -> bool:
        return any(entry["room_id"] == room_id for entry in self._entries)

    def next_guest(self, room_id: int):
        for entry in self._entries:
            if entry["room_id"] == room_id:
                return entry["guest_id"]
        return None

    def remove_entry(self, guest_id: int, room_id: int) -> None:
        for index, entry in enumerate(self._entries):
            if entry["guest_id"] == guest_id and entry["room_id"] == room_id:
                del self._entries[index]
                return
        raise ValueError("Waitlist entry not found")
