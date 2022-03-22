from datetime import date

class Reservation:
    def __init__(self, numero_chambre : int, date_debut : date, date_fin : date, nombre_personnes=0) -> None:
        self.numero_chambre = numero_chambre
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_personnes = nombre_personnes