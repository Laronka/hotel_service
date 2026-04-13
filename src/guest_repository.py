class GuestRepository:
    def __init__(self):
        self._guests = {
            1: {"name": "Alice", "blocked": False, "pending_debt": False},
            2: {"name": "Bruno", "blocked": True, "pending_debt": False},
            3: {"name": "Carla", "blocked": False, "pending_debt": True},
            4: {"name": "Diego", "blocked": False, "pending_debt": False},
        }

    def exists(self, guest_id: int) -> bool:
        return guest_id in self._guests

    def is_blocked(self, guest_id: int) -> bool:
        if guest_id not in self._guests:
            return False
        return self._guests[guest_id]["blocked"]

    def has_pending_debt(self, guest_id: int) -> bool:
        if guest_id not in self._guests:
            return False
        return self._guests[guest_id]["pending_debt"]
