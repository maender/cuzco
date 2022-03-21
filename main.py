from modules.chambres import Chambre
from modules.hotel import Hotel
from user_side.interfaces import AfficheurChambres


chambres = [
    Chambre(1, 101, "chambre avec balcon", 2),
    Chambre(2, 201, "chambre avec vue sur piscine", 1)
]

# Hotel(chambres, AfficheurChambres()).afficherChambres()
chambres = [
            Chambre(1, 101, "chambre avec balcon", 2),
            Chambre(2, 201, "chambre avec vue sur piscine", 1)]
print('\n'.join([c.toStr() for c in chambres]))