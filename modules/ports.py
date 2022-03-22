from modules.chambres import Chambre

class PortAffichage:
    def afficher(self, chambres):
        pass

class PortChambresDataSource:
    def recupererChambres(self):
        pass

class ReservationsDataSource:
    def recupererReservations(self):
        pass

    def ajouterReservation(self, numero_chambre, date_debut, date_fin):
        pass

class PortReservation:
    def chercherChambresDisponibles(self, date_debut, date_fin, nombre_personnes):
        pass

    def reserverChambre(self, numero_chambre, date_debut, date_fin):
        pass
