import re
from modules.chambres import Chambre
from modules.ports import PortAffichage

class AfficheurAdapter(PortAffichage):
    def afficherChambres(self, chambres):
        if chambres is not None:
            for chambre in chambres:
                print(chambre)
        else:
            print("Pas de chambres disponibles")

    def afficherMessage(self, message):
        print(message)

    def afficherReservations(self, reservations):
        if len(reservations) > 0:
            for reservation in reservations:
                print('Chambre {} réservée du {} au {}'.format(reservation.numero_chambre, reservation.date_debut, reservation.date_fin))
