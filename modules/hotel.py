from datetime import date, timedelta
from modules.chambres import Chambre

class Hotel:
    def __init__(self, port_affichage=None, port_chambres_data_source=None, port_reservation_data_source=None) -> None:
        self.port_affichage = port_affichage
        self.port_chambres_data_source = port_chambres_data_source
        self.port_reservation_data_source = port_reservation_data_source

    def afficherChambres(self):
        chambres = self.port_chambres_data_source.recupererChambres()
        self.port_affichage.afficherChambres(chambres)

    def recupererChambresDisponibles(self, chambres, date_debut, date_fin, nombre_personnes):
        numero_chambres_non_disponibles = list()
        reservations = self.port_reservation_data_source.recupererReservations()
        for reservation in reservations:
            if date_debut >= reservation.date_debut and date_debut <= reservation.date_fin:
                if reservation.numero_chambre not in numero_chambres_non_disponibles:
                    numero_chambres_non_disponibles.append(reservation.numero_chambre)
            elif date_fin >= reservation.date_debut and date_fin <= reservation.date_fin:
                if reservation.numero_chambre not in numero_chambres_non_disponibles:
                    numero_chambres_non_disponibles.append(reservation.numero_chambre)
        chambres_disponibles = [chambre for chambre in chambres if chambre.numero not in numero_chambres_non_disponibles]
        if sum([chambre.capacite for chambre in chambres_disponibles]) >= nombre_personnes:
            return chambres_disponibles
        else:
            return None

    def afficherChambresDisponibles(self, date_debut:date, date_fin:date, nombre_personnes):
        chambres_disponibles = self.recupererChambresDisponibles(date_debut, date_fin, nombre_personnes)
        self.port_affichage.afficherChambres(chambres_disponibles)

    def afficherChambresDisponibles(self, date_debut, date_fin, nombre_personnes):
        chambres = self.port_chambres_data_source.recupererChambres()
        chambres_disponibles = self.recupererChambresDisponibles(chambres, date_debut, date_fin, nombre_personnes)
        self.port_affichage.afficher(chambres_disponibles)
