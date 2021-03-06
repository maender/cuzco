from modules.reservation import Reservation
from modules.ports import ReservationsDataSource
from datetime import date, timedelta

class ReservationDataSourceAdapter(ReservationsDataSource):
    def __init__(self) -> None:
        self.liste_reservations = [
            Reservation(101, date(2022, 5, 3), date(2022, 5, 10))
        ]

    def recupererReservations(self):
        return self.liste_reservations

    def ajouterReservation(self, numero_chambre, date_debut, date_fin):
         self.liste_reservations.append(
             Reservation(numero_chambre, date_debut, date_fin)
        )