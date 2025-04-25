from DomesticFlight import DomesticFlight
from InternationalFlight import InternationalFlight
from Airline import Airline



class BookingSystem:
    def __init__(self):
        self.airline = Airline("Wizz Air")
        self._init_data()

    def _init_data(self):
        self.airline.flights = DomesticFlight("W62112", "Budapest", "Debrecen", "2025-06-15 06:00", 5000, True)
        self.airline.flights = DomesticFlight("W62123", "Debrecen", "Pér", "2025-06-16 09:00", 4500, True)
        self.airline.flights = DomesticFlight("W62333", "Pécs", "Budapest", "2025-06-18 12:00", 3500, False)
        self.airline.flights = DomesticFlight("W62344", "Budapest", "Debrecen", "2025-06-19 15:00", 6000, True)

        self.airline.flights = InternationalFlight("W62312", "Budapest", "London", "2025-06-12 06:00", 15000, True)
        self.airline.flights = InternationalFlight("W62323", "London", "Paris", "2025-06-13 09:00", 18000, True)
        self.airline.flights = InternationalFlight("W62334", "Paris", "Budapest", "2025-06-14 12:00", 20000, False)
        self.airline.flights = InternationalFlight("W62345", "Budapest", "Madrid", "2025-06-18 15:00", 25000, False)
        self.airline.flights = InternationalFlight("W62356", "Budapest", "Róma", "2025-06-19 18:00", 30000, True)

    def MainMenu(self) -> None:

        while True:

            try:

                menu = int(input("""\nFőmenü:
                        1-es billentyű: Foglalások listázása
                        2-es billentyű: Járat foglalása
                        3-as billentyű: Foglalás lemondása
                        0-s billentyű: Kilépés

                        Melyik menüpontot választja? """))

                match menu:
                    case 1:
                        self.airline.list_flights()
                    case 2:
                        flight = input("Kérem adja meg járatszámot a foglaláshoz: ").strip()
                        self.airline.book_by_flight_number(flight)

                    case 3:
                        flight = input("Kérem adja meg a lemondani kívánt járat számát: ").strip()
                        self.airline.unbook_by_flight_number(flight)

                    case 0:
                        print("Kilépés a programból.")
                        exit()
                    case _:
                        print("Érvénytelen menüpont! Próbálja újra.")
            except ValueError:
                print("Hiba: Csak számokat adjon meg a menüpont kiválasztásához.")

booking_system = BookingSystem()
booking_system.MainMenu()
