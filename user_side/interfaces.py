from modules import chambres
from modules.chambres import Chambre
from modules.ports import PortAffichage


class AfficheurChambres(PortAffichage):
    def get_attributes_names(self, chambres : list):
        return [x for x in chambres[0].__dict__.keys()]

    def get_max_param_sizes(self, chambres : list, attributes : list):
        max_attributes_size = [0 for x in range(len(attributes))]
        for chambre in chambres:
            for i, attr in enumerate(attributes):
                max_attributes_size[i] = max(len(str(getattr(chambre, attr))), len(attr))
        return max_attributes_size


    def afficher(self, chambres):
        out = ''
        if len(chambres) <= 0:
            pass
        attributes_names = self.get_attributes_names(chambres)
        max_attributes_size = self.get_max_param_sizes(chambres, attributes_names)
        word =  '{:{align}{width}s}'
        out += '| '
        for i, attr in enumerate(attributes_names):
            out += word.format(attr, align='<', width=max_attributes_size[i]) + (' | ' if i < len(attributes_names) - 1 else ' |\n')
            attributes_names[i] = word
        out += '|'
        for i in range(len(attributes_names)):
            out += ':' + "-" * max_attributes_size[i] + ':' + '|'
        out += '\n'
        for i, chambre in enumerate(chambres):
            if i > 0:
                out += '\n'
            out += '| '
            out += str(chambre.etage).center(max_attributes_size[0]) + ' | '
            out += word.format(str(chambre.numero), align='<', width=max_attributes_size[1]) + ' | '
            out += word.format(str(chambre.description), align='<', width=max_attributes_size[2]) + ' | '
            out += word.format(str(chambre.capacite), align='<', width=max_attributes_size[3]) + ' |'
        print(out)
