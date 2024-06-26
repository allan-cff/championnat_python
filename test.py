from Sportif import Personne, Sportif
from Equipe import Equipe


def tests_personne():
    clara = Personne("Clara", 12)
    print(clara)

    jojo = Sportif("Jojo", 12, "basket")
    print(jojo)


def tests_equipe():
    equipe_0 = Equipe('basket', 'les foufous', ('luc', 'david', 'fronçois'))
    equipe_0.show_team_name()
    equipe_0.show_team_members()


tests_equipe()
tests_personne()
