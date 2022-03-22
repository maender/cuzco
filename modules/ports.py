from modules.chambres import Chambre

class PortAffichage:
    def afficherChambres(self, chambres):
        pass

    def afficherMessage(self, message):
        pass

    def afficherReservations(self, reservations):
        pass

class PortChambresDataSource:
    def recupererChambres(self):
        pass

    def recupererChambreParSonNumero(self, numero_chambre):
        pass

class ReservationsDataSource:
    def recupererReservations(self):
        pass

    def ajouterReservation(self, date_debut, date_fin, numero_chambre, nimbre_personnes):
        pass

class PortReservation:
    def chercherChambresDisponibles(self, date_debut, date_fin, nombre_personnes):
        pass

    def reserverChambre(self, numero_chambre, date_debut, date_fin):
        pass
