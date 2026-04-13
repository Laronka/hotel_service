class HotelService:
    def __init__(self, room_repository, guest_repository, stay_repository, waitlist_repository):
        self.room_repository = room_repository
        self.guest_repository = guest_repository
        self.stay_repository = stay_repository
        self.waitlist_repository = waitlist_repository

    def check_in(self, guest_id: int, room_id: int) -> bool:
        if not guest_id or not room_id:
            raise ValueError("Guest ID and room ID are required")

        if not self.guest_repository.exists(guest_id):
            return False

        if not self.room_repository.exists(room_id):
            return False

        if self.guest_repository.is_blocked(guest_id):
            return False

        if self.guest_repository.has_pending_debt(guest_id):
            return False

        if not self.room_repository.is_available(room_id):
            return False

        if self.stay_repository.count_active_stays(guest_id) >= 2:
            return False

        next_guest = self.waitlist_repository.next_guest(room_id)
        if next_guest is not None and next_guest != guest_id:
            return False

        self.room_repository.mark_unavailable(room_id)
        self.stay_repository.create_stay(guest_id, room_id)

        if self.waitlist_repository.has_entry(guest_id, room_id):
            self.waitlist_repository.remove_entry(guest_id, room_id)

        return True

    def check_out(self, guest_id: int, room_id: int) -> bool:
        if not guest_id or not room_id:
            raise ValueError("Guest ID and room ID are required")

        if not self.stay_repository.is_room_with_guest(guest_id, room_id):
            return False

        self.stay_repository.close_stay(guest_id, room_id)

        if self.waitlist_repository.has_any_entry(room_id):
            self.room_repository.mark_unavailable(room_id)
        else:
            self.room_repository.mark_available(room_id)

        return True

    def join_waitlist(self, guest_id: int, room_id: int) -> bool:
        if not guest_id or not room_id:
            raise ValueError("Guest ID and room ID are required")

        if not self.guest_repository.exists(guest_id):
            return False

        if not self.room_repository.exists(room_id):
            return False

        if self.guest_repository.is_blocked(guest_id):
            return False

        if self.guest_repository.has_pending_debt(guest_id):
            return False

        if self.room_repository.is_available(room_id):
            return False

        if self.waitlist_repository.has_entry(guest_id, room_id):
            return False

        if self.stay_repository.is_room_with_guest(guest_id, room_id):
            return False

        self.waitlist_repository.add_entry(guest_id, room_id)
        return True
