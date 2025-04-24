from Flight import Flight

class InternationalFlight(Flight):
    def __init__(self, flight_number, departure_airport, arrival_airport, departure_date, price, booked):
        super().__init__(flight_number, departure_airport, arrival_airport, departure_date, price, booked)

    def book_flight(self):
        self.is_booked = True
        print(f"A {self.flight_number} járat sikeresen lefoglalva.")
        return True

    def unbook_flight(self):
        self.is_booked = False
        print(f"A {self.flight_number} járat foglalása sikeresen törölve.")
        return True