import csv
import os

# create player class

# extract each row of each input file into player class

# add each player to array displaying important stats

class Player:
    def __init__(self, id, season, name, team, games_played, goals, assists, points, powerplay_goals, shorthanded_goals, shots, hits, blocks):
        self.id = id
        self.season = (season)
        self.name = (name)
        self.team = (team)
        self.games_played = (games_played)
        self.goals = (goals)
        self.assists = (assists)
        self.points = (points)
        self.powerplay_goals = (powerplay_goals)
        self.shorthanded_goals = (shorthanded_goals)
        self.shots = (shots)
        self.hits = (hits)
        self.blocks = (blocks)

    def __str__(self):
        return self.name + " " + self.season + " " + self.games_played + "GP " + self.goals + "G " + self.assists + "A " + self.points + "P " + self.powerplay_goals + "PPG " + self.shorthanded_goals + "SHG " + self.shots + "SOG " + self.hits + "H " + self.blocks + "B "

player_array = []

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '../res/moneypuck/moneypuck_2023-24.csv')

with open(file_path) as file: 
    reader = csv.reader(file)
    for row in reader:
        if (row[5] == 'all'): # all situations
            id = row[0]
            season = row[1]
            name = row[2]
            team = row[3]
            games_played = row[6]
            goals = row[34]
            assists = str(float(row[27])+float(row[28]))
            points = row[33]
            shots = row[29]
            hits = row[46]
            blocks = row[83]
        elif (row[5] == '5on4'): # powerplay
            powerplay_goals = row[34]
        elif (row[5] == '4on5'): # shorthanded
            shorthanded_goals = row[34]
        
        current_player = Player(id, season, name, team, games_played, goals, assists, points, powerplay_goals, shorthanded_goals, shots, hits, blocks)
        print(current_player)