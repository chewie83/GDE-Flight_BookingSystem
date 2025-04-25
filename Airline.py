class Airline:
    def __init__(self, name: str):
        self._name = name
        self._flights = []

    @property
    def name(self):
        return self._name

    @property
    def flights(self):
        return self._flights


    @flights.setter
    def flights(self, new_flight):
        self._flights.append(new_flight)

    def list_flights(self):
        for flight in self._flights:
            print(f"Flight number: {flight.flight_number}, Departure: {flight.departure_airport}, "
                  f"Arrival: {flight.arrival_airport}, Departure date: {flight.departure_date}, "
                  f"Price: {flight.price}, Booked: {'Yes' if flight.is_booked else 'No'}")

        def book_by_flight_number(self, flight_number):
        for flight in self._flights:
            if flight.flight_number == flight_number:
                if flight.is_booked:
                    print("Már foglalt ez a járat.")
                    return False
                else:
                    return flight.book_flight()
        print("Nincs ilyen járat vagy rosszul adta meg a járatszámot!")
        return False

    def unbook_by_flight_number(self, flight_number):
        for flight in self._flights:
            if flight.flight_number == flight_number:
                if not flight.is_booked:
                    print("Ez a járat jelenleg nincs lefoglalva.")
                    return False
                else:
                    return flight.unbook_flight()
        print("Nincs ilyen járat vagy rosszul adta meg a járatszámot!")
        return False
