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

class PortReservationsDataSource:
    def recupererReservations(self):
        pass

    def ajouterReservation(self, date_debut, date_fin, numero_chambre, nimbre_personnes):
        pass
