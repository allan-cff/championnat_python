from Sportif import Personne, Sportif
from Equipe import Equipe
from Championnat import *


def tests_personne():
    clara = Personne("Clara", 12)
    print(clara)

    jojo = Sportif("Jojo", 12, "basket")
    print(jojo)


def tests_equipe():
    luc = Sportif("Luc", 12, "basket")
    david = Sportif("David", 12, "basket")
    francois = Sportif("François", 12, "basket")

    equipe_0 = Equipe('basket', 'les foufous', (luc, david, francois))
    print(equipe_0)

def tests_championnat():
    luc = Sportif("Luc", 12, "basket")
    david = Sportif("David", 12, "basket")
    francois = Sportif("François", 18, "basket")
    equipe0 = Equipe('basket', 'les foufous', (luc, david, francois))
    equipe1 = Equipe('basket', 'les fou', ('lucas', 'marc', 'didier'))
    print(equipe0)
    print(equipe1)


#tests_equipe()
#tests_personne()
tests_championnat()
