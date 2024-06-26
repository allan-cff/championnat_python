class Equipe():
    def __init__(self, sport, name, team_members):
        self.sport = sport
        self.name = name
        self.team_members = team_members
    def show_team_members(self):
        print(self.team_members)
    def show_team_name(self):
        print(self.name)
equipe_0 = Equipe('basket', 'les foufous', ('luc', 'david', 'fronçois'))
equipe_0.show_team_name()
equipe_0.show_team_members()
print("test")