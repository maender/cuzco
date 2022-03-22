from modules.chambres import Chambre
from modules.ports import PortChambresDataSource
from datetime import date, timedelta

class ChambresDataSourceAdapter(PortChambresDataSource):
    def __init__(self) -> None:
        self.liste_chambres = [
            Chambre(1, 101, "1 King size bed - A/C - Wi-Fi - private bathroom - wheelchair accessible", 2),
            Chambre(1, 102, "2 queen size beds - A/C - Wi-Fi - private bathroom - wheelchair accessible", 4),
            Chambre(1, 103, "3 single beds - A/C - Wi-Fi - private bathroom - wheelchair accessible", 3),
            Chambre(2, 201, "1 king size bed - A/C - Wi-Fi - private bathroom", 2),
            Chambre(2, 202, "1 queen size bed - Wi-Fi - private bathroom", 2),
            Chambre(2, 203, "1 king size bed + 3 single beds - A/C - Wi-Fi - private bathroom", 5),
            Chambre(2, 204, "1 single bed - Wi-Fi - shared bathroom", 1),
            Chambre(2, 205, "2 single beds - A/C - Wi-Fi - shared bathroom", 2),
            Chambre(3, 301, "1 queen size bed - A/C - private bathroom", 2),
            Chambre(3, 302, "2 single beds - A/C - private bathroom", 2),
            Chambre(3, 303, "3 single beds - A/C - shared bathroom", 3),
            Chambre(3, 304, "2 single beds - shared bathroom", 2)
        ]

    def recupererChambres(self):
        return self.liste_chambres