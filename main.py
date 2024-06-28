#from Championnat import *
import time
def createTeams(sport):
    team_list = []
    number_of_teams = int(input("How many teams do you want to create? "))
    for i in range(number_of_teams):
        print("Creating team " + str(i + 1) + "...")
        name = input("What is team name ? ")
        team_members = ()
        for j in range(4):
            people = input("What is team member name ? ")
            team_members = team_members + (people,)
        team_list.append(Equipe(sport, name, team_members))
    return team_list

def simu():
    print("                     ------Simulating Championship matchs ------\n")
    time.sleep(1)
    print("                     ------Simulating Championship matchs. -----\n")
    time.sleep(1)
    print("                     ------Simulating Championship matchs.. ----\n")
    time.sleep(1)
    print("                     ------Simulating Championship matchs... ---\n")
    time.sleep(1.5)
    print("                     The championship matchs are now simulated !\n")
    time.sleep(1.5)

sport = input('Witch sport the championship is ? ')
#championship = Championnat(sport, createTeams(sport))       #championat creation
simu()                                                      #delay (fun)
# championship.simulate_all_matches()