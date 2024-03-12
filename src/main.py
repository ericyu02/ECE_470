import csv
import os
import pprint

# create player class

# extract each row of each input file into player class

# add each player to array displaying important stats

class Player:
    def __init__(self, id, season, name, team, games_played, goals, assists, points, powerplay_goals, shorthanded_goals, special_goals, shots, hits, blocks):
        self.id = int(id)
        self.season = str(int(season)) + '-' + str((int(season) + 1))[-2:]
        self.name = str(name)
        self.team = str(team)
        self.games_played = int(games_played)
        self.goals = int(goals)
        self.assists = int(assists)
        self.points = int(points)
        self.powerplay_goals = int(powerplay_goals)
        self.shorthanded_goals = int(shorthanded_goals)
        self.special_goals = int(special_goals)
        self.shots = int(shots)
        self.hits = int(hits)
        self.blocks = int(blocks)

    def __str__(self):
        return str(self.name) + " " + str(self.season) + " " + str(self.games_played) + "GP " + str(self.goals) + "G " + str(self.assists) + "A " + str(self.points) + "P " + str(self.powerplay_goals) + "PPG " + str(self.shorthanded_goals) + "SHG " + str(self.special_goals) + "SG " + str(self.shots) + "SOG " + str(self.hits) + "H " + str(self.blocks) + "B"
    
    __repr__ = __str__
    
season_dictionary = {}

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '../res/moneypuck/moneypuck_2023-24.csv')

with open(file_path) as file: 
    reader = csv.reader(file)
    headers = next(reader) 
    for row in reader:
        # create dictionary entry
        id = int(row[0])
        if id not in season_dictionary:
            season_dictionary[id] = Player(id, '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0')
        
        # all situations
        if (row[5] == 'all'):
            season_dictionary[id].season = int(float(row[1]))
            season_dictionary[id].name = str(row[2])
            season_dictionary[id].team = str(row[3])
            season_dictionary[id].games_played = int(float(row[6]))
            season_dictionary[id].goals = int(float(row[34]))
            season_dictionary[id].assists = int(float(row[27])+float(row[28]))
            season_dictionary[id].points = int(float(row[33]))
            season_dictionary[id].shots = int(float(row[29]))
            season_dictionary[id].hits = int(float(row[46]))
            season_dictionary[id].blocks = int(float(row[83]))

        # powerplay (5on4 only)
        elif (row[5] == '5on4'):
            season_dictionary[id].powerplay_goals = int(float(row[34]))

        # shorthanded (4on5 only)
        elif (row[5] == '4on5'):
            season_dictionary[id].shorthanded_goals = int(float(row[34]))
        
        # all other situations (5on3, 6on5, 3on3, etc.)
        elif (row[5] == 'other'):
            season_dictionary[id].special_goals = int(float(row[34]))

    pprint.pprint(season_dictionary)