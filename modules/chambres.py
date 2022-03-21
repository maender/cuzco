class Chambre:
    def __init__(self,etage:int,numero:int,description:str,capacite:int):
        self.etage = etage
        self.numero = numero
        self.description =description
        self.capacite = capacite

    def __repr__(self) -> str:
        return '{}\t{}\t{}\t{}\n'.format(self.etage, self.numero, self.description, self.capacite)

    def afficher_chambre(self):
        return self.__repr__()