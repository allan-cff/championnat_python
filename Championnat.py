from Equipe import *
from Sportif import *
from numpy import random

class Championnat():
    def __init__(self, sport, teams=[]):
        self.teams = teams
        self.sport = sport
        self.matchlist = []
        self.points = {}
        self.classement = {}
        self.result = {}
    def add_teams(self, team):
        self.teams.append(team)

    def show_all_teams(self): #pour toutes les equipes
        affiche = f"Le championnat est composé de :"
        for equipe in self.teams:
            affiche += str(equipe)
        return affiche

    def add_all_teams(self, *teams):
        for i in range(len(teams)):
            self.teams.append(teams[i])


    def display_classement(self):
        for i in range(len(self.teams)):
            pass



    def update_values(self):
        for match in self.matchlist:
            if match.ended:
                # Match terminé donc on place les équipes dans les variables points classements et results
                team1, team2 = match.get_teams()
                if not team1 in self.points:
                    self.points[team1] = 0
                if not team2 in self.points:
                    self.points[team2] = 0
                if not team1 in self.classement:
                    self.points[team1] = 0
                if not team2 in self.classement:
                    self.points[team2] = 0
                if not team1 in self.result:
                    self.result[team1] = {team2: match}
                if not team2 in self.result:
                    self.result[team2] = {team1: match}
                if not team1 in self.result[team2]:
                    self.result[team1][team2] = match
                if not team2 in self.result[team1]:
                    self.result[team2][team1] = match
                # On ajoute les points aux équipes
                if match.is_tie():
                    self.points[team1] += 1
                    self.points[team2] += 1
                else:
                    winner = match.get_winner()
                    if winner == team1:
                        self.points[team1] += 3
                    else:
                        self.points[team2] += 3
        # On modifie le classement
        for team, points in self.points.items():
            pass




    def create_all_matches(self):
        for i in range(len(self.teams)):
            for j in range(i+1, len(self.teams)):
                self.matchlist.append(Match(self.teams[i], self.teams[j]))

    def simulate_all_matches(self):
        self.create_all_matches()
        self.show_all_teams()
        for match in self.matchlist:
            match.random_score()

    def get_results_csv(self):
        result = f"team;{';'.join(map(lambda team: team.name, self.teams))};total buts;total points;classement\n"
        for team in self.teams:
            result += f"{team.name};"
            total_score = 0
            for teamb in self.teams:
                if team != teamb:
                    score = self.results[team][teamb].get_score(team)
                    total_score += score
                    result += f"{score};"
                else:
                    result += "N/A;"
            result += f"{total_score};{self.points[team]};{self.classement[team]}\n"
        return result

class Match():
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.score1 = 0
        self.score2 = 0
        self.ended = False

    def get_teams(self):
        return self.team1, self.team2

    def get_score(self):
        return self.score1, self.score2

    def get_team_score(self, team):
        if team == self.team1:
            return self.score1
        else:
            return self.score2

    def is_tie(self):
        return self.score1 == self.score2 #ressort un bouleen

    def get_winner(self):
        if not self.is_tie(): #si ce n'est une egalite, c'est à dire que ce n'est pas true
            if self.score1 > self.score2:
                return self.team1
            else:
                return self.team2
        else:
            return None

    def set_score(self, score1, score2):
        self.score1 = score1
        self.score2 = score2

    def random_score(self):
        self.set_score(random.normal(self.team1.average_score, 4), random.normal(self.team2.average_score, 4))
        self.ended = True
