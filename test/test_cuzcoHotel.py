import unittest
from modules.hotel import Hotel
from modules.chambres import Chambre
from modules.ports import *
from user_side.afficheurAdapter import AfficheurAdapter
from server_side.chambresDataSourceAdapter import ChambresDataSourceAdapter
from server_side.reservationsDataSourceAdapter import ReservationDataSourceAdapter
from datetime import date

chambres_test = [
    "1\t101\t1 King size bed - A/C - Wi-Fi - private bathroom - wheelchair accessible\t2\n",
    "1\t102\t2 queen size beds - A/C - Wi-Fi - private bathroom - wheelchair accessible\t4\n",
    "1\t103\t3 single beds - A/C - Wi-Fi - private bathroom - wheelchair accessible\t3\n",
    "2\t201\t1 king size bed - A/C - Wi-Fi - private bathroom\t2\n",
    "2\t202\t1 queen size bed - Wi-Fi - private bathroom\t2\n",
    "2\t203\t1 king size bed + 3 single beds - A/C - Wi-Fi - private bathroom\t5\n",
    "2\t204\t1 single bed - Wi-Fi - shared bathroom\t1\n",
    "2\t205\t2 single beds - A/C - Wi-Fi - shared bathroom\t2\n",
    "3\t301\t1 queen size bed - A/C - private bathroom\t2\n",
    "3\t302\t2 single beds - A/C - private bathroom\t2\n",
    "3\t303\t3 single beds - A/C - shared bathroom\t3\n",
    "3\t304\t2 single beds - shared bathroom\t2\n"
]

class TestHotel(unittest.TestCase):
    # def testAffichageChambres(self):
    #     self.assertEqual(
    #     '\n'.join([c.afficher_chambre() for c in ChambresDataSourceAdapter().recupererChambres()]) + '\n',
    #     ''.join([c for c in chambres_test])
    #     )

    # def testAffichage(self):
    #     sp = SpyAfficheur()
    #     cuzco = Hotel(sp, ChambresDataSourceAdapter())
    #     cuzco.afficherChambres()
    #     self.assertEqual(
    #         sp.dernier_output,
    #         "".join(chambres_test)
    #     )
    #     self.assertEqual(
    #         sp.compteur_appel,
    #         1
    #     )

    def testAfficherChambresDisponibles(self):
        sp = SpyAfficheur()
        cuzco = Hotel(AfficheurAdapter(), ChambresDataSourceAdapter(), ReservationDataSourceAdapter())
        cuzco.afficherChambresDisponibles(date(2022, 5, 3), date(2022, 5, 27), 10)
        # self.assertEqual(
        #     sp.dernier_output,
        #     "".join(chambres_test)
        # )
        # self.assertEqual(
        #     sp.compteur_appel,
        #     2
        # )

if __name__ == '__main__':
    unittest.main()

class SpyAfficheur(PortAffichage):
    def __init__(self) -> None:
        super().__init__()
        self.compteur_appel = 0
        self.dernier_output = ''

    def afficherChambres(self, chambres : list):
        self.dernier_output = ''
        for chambre in chambres:
            self.dernier_output += chambre.afficher_chambre() + '\n'
        print(self.dernier_output)
        self.compteur_appel += 1

    def afficherMessage(self, message):
        self.dernier_output = message
        print(self.dernier_output)
        self.compteur_appel += 1
