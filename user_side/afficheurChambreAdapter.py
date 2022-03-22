from modules.chambres import Chambre
from modules.ports import PortAffichage, PortReservation

class AfficheurChambres(PortAffichage):
    def afficher(self, chambres):
        if chambres is not None:
            for chambre in chambres:
                print(chambre)
        else:
            print("Pas de chambres disponibles")
