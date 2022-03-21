from modules.chambres import Chambre
from modules.ports import PortAffichage

class AfficheurChambres(PortAffichage):
    def afficher(self, chambres):
        for chambre in chambres:
            print(chambre)