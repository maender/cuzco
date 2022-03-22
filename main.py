from modules.chambres import Chambre
from modules.hotel import Hotel
from user_side.interfaces import AfficheurChambres


chambres = [
    Chambre(1, 101, "chambre avec balcon", 2),
    Chambre(2, 201, "chambre avec vue sur piscine et superbe lit royal décorée d'or et de diamants", 1)
]

Hotel(chambres, AfficheurChambres()).afficherChambres()
