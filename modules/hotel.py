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


    def recupererChambreParSonNumero(self, numerochambre):
        return self.port_chambres_data_source.recupererChambreParSonNumero(numerochambre)


    def verifierDatesIndisponibles(self, reservation, date_debut:date, date_fin:date, numero_chambres_non_disponibles):
        if ((date_debut >= reservation.date_debut and date_debut <= reservation.date_fin)
            or (date_fin >= reservation.date_debut and date_fin <= reservation.date_fin)):
                if reservation.numero_chambre not in numero_chambres_non_disponibles:
                    return True
        return False


    def listeChambresPouvantHebergerNombreDePersonnes(self, chambres_disponibles, nombre_personnes):
        if sum([chambre.capacite for chambre in chambres_disponibles]) >= nombre_personnes:
            return chambres_disponibles
        else:
            return None


    def recupererChambresIndisponibles(self, date_debut:date, date_fin:date):
        numero_chambres_non_disponibles = list()
        reservations = self.port_reservation_data_source.recupererReservations()

        for reservation in reservations:
            if self.verifierDatesIndisponibles(reservation, date_debut, date_fin, numero_chambres_non_disponibles):
                numero_chambres_non_disponibles.append(reservation.numero_chambre)
        return numero_chambres_non_disponibles


    def recupererChambresDisponibles(self, date_debut:date, date_fin:date, nombre_personnes):
        chambres = self.port_chambres_data_source.recupererChambres()
        numero_chambres_non_disponibles = self.recupererChambresIndisponibles(date_debut, date_fin)

        chambres_disponibles = [chambre for chambre in chambres if chambre.numero not in numero_chambres_non_disponibles]
        return self.listeChambresPouvantHebergerNombreDePersonnes(chambres_disponibles, nombre_personnes)


    def afficherChambresDisponibles(self, date_debut:date, date_fin:date, nombre_personnes):
        chambres_disponibles = self.recupererChambresDisponibles(date_debut, date_fin, nombre_personnes)
        self.port_affichage.afficherChambres(chambres_disponibles)


    def verifierMauvaisesDates(self, date_debut, date_fin):
        if date_fin - date_debut < timedelta(days=1):
            return True
        return False


    def verifierReservationPossible(self, date_debut, date_fin, numero_chambre, nombre_perosonnes):
        chambre_voulue = self.recupererChambreParSonNumero(numero_chambre)
        numero_chambres_non_disponibles = self.recupererChambresIndisponibles(date_debut, date_fin)
        message = None
        if self.verifierMauvaisesDates(date_debut, date_fin):
            message = 'La réservation doit faire au minimum un jour complet'
        elif chambre_voulue is None:
            message = "Cette chambre n'existe pas"
        elif numero_chambre in numero_chambres_non_disponibles:
            message = 'Chambre non disponible sur la période donnée'
        elif chambre_voulue.capacite < nombre_perosonnes:
            message = 'La chambre désirée ne possède pas assez de place'

        return message


    def ajouterReservation(self, date_debut:date, date_fin:date, numero_chambre, nombre_personnes):
        message = self.verifierReservationPossible(date_debut, date_fin, numero_chambre, nombre_personnes)
        if message is not None:
            self.port_affichage.afficherMessage(message)
        else:
            self.port_reservation_data_source.ajouterReservation(date_debut, date_fin, numero_chambre, nombre_personnes)
            self.port_affichage.afficherMessage('La réservation a bien été enregistrée')


    def afficherReservations(self):
        reservations = self.port_reservation_data_source.recupererReservations()
        self.port_affichage.afficherReservations(reservations)