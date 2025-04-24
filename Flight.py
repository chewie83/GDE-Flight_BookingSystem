from abc import ABC, abstractmethod

class Flight(ABC):
    def __init__(self, flight_number: str, departure_airport: str, arrival_airport: str, departure_date: str, price: int, is_booked: bool):
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_date = departure_date
        self.price = price
        self.is_booked = is_booked


    @abstractmethod
    def book_flight(self):
        pass
    @abstractmethod
    def unbook_flight(self):
        pass


