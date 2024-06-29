class Equipe():
    def __init__(self, sport, name, team_members):
        self.sport = sport
        self.name = name
        self.team_members = team_members
        self.average_score = 0

    def __str__(self):
        result = f"L'équipe {self.name} ({self.sport}) est constituée des joueurs suivants : "
        for joueur in self.team_members: #récupère les valeurs dans la liste des team_members
            result += joueur.name + ", " #ajoute les joueurs et met une virgule
        return result
