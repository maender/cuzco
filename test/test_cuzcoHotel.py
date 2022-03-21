import unittest
from modules.hotel import Hotel
from modules.chambres import Chambre
from modules.ports import *
from user_side.interfaces import AfficheurChambres

chambres = [
    Chambre(1, 101, "chambre avec balcon", 2),
    Chambre(2, 201, "chambre avec vue sur piscine", 1)]
chambres_test = [
    "1\t101\tchambre avec balcon\t2\n",
    "2\t201\tchambre avec vue sur piscine\t1\n"
]


'''
JL le problème dans les tests venait du fait que les join() ne mettent pas
le charactère après la derniere string de la liste et donc il n'y avait pas de \n à la fin
J'ai corrigé ça mais ça rend le truc un peu chelou donc je pense que ce serait plus simple de faire
la chaine globale 'à la main' ce qui évitera ces problèmes.
'''

class TestHotel(unittest.TestCase):
    def testAffichageChambres(self):
        self.assertEqual(
        '\n'.join([c.afficher_chambre() for c in chambres]) + '\n',
        ''.join([c for c in chambres_test])
        )

    def testAffichage(self):
        sp = SpyAfficheur()
        cuzco = Hotel(chambres, sp)
        cuzco.afficherChambres()
        self.assertEqual(
            sp.dernier_output,
            "".join(chambres_test)
        )
        self.assertEqual(
            sp.compteur_appel,
            1
        )

if __name__ == '__main__':
    unittest.main()

class SpyAfficheur(PortAffichage):
    def __init__(self) -> None:
        super().__init__()
        self.compteur_appel = 0
        self.dernier_output = ''

    def afficher(self, chambres : list):
        self.dernier_output = ''
        for chambre in chambres:
            self.dernier_output += chambre.afficher_chambre() + '\n'
        print(self.dernier_output)
        self.compteur_appel += 1
