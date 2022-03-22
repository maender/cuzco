import re
from modules.chambres import Chambre
from modules.ports import PortAffichage, PortReservation

class AfficheurAdapter(PortAffichage):
    def afficher(self, chambres):
        if chambres is not None:
            for chambre in chambres:
                print(chambre)
        else:
            print("Pas de chambres disponibles")
