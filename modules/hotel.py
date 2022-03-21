from modules.chambres import Chambre

class Hotel:
    def __init__(self, chambres : list, port_affichage=None) -> None:
        self.chambres = chambres
        self.port_affichage = port_affichage

    def afficherChambres(self):
        self.port_affichage.afficher(self.chambres)
