import csv
import os
import pprint

class Player:
    def __init__(self, id='0000000', season='0000', name='NAME', team='TEAM', position='POS', games_played='0', goals='0', assists='0', points='0', powerplay_goals='0', shorthanded_goals='0', special_goals='0', expected_goals = '0', shots='0', hits='0', blocks='0', fantasy_score='0'):
        self.id = int(id)
        self.season = int(season)
        self.name = str(name)
        self.team = str(team)
        self.position = str(position)
        self.games_played = float(games_played)
        self.goals = float(goals)
        self.assists = float(assists)
        self.points = float(points)
        self.powerplay_goals = float(powerplay_goals)
        self.shorthanded_goals = float(shorthanded_goals)
        self.special_goals = float(special_goals)
        self.expected_goals = float(expected_goals)
        self.shots = float(shots)
        self.hits = float(hits)
        self.blocks = float(blocks)
        self.fantasy_score = float(fantasy_score)

    def round_stats(self):
        self.goals = round(self.goals)
        self.assists = round(self.assists)
        self.points = self.goals + self.assists
        self.powerplay_goals = round(self.powerplay_goals)
        self.shorthanded_goals = round(self.shorthanded_goals)
        self.shots = round(self.shots)
        self.hits = round(self.hits)
        self.blocks = round(self.blocks)
        self.fantasy_score = round(self.fantasy_score, 1)
        return self

    def __str__(self):
        return str(self.name) + " " + str(self.position) + " " + str(self.season) + '-' + str(self.season + 1)[-2:] + " " + str(self.games_played) + "GP " + str(self.goals) + "G " + str(self.assists) + "A " + str(self.points) + "P " + str(self.powerplay_goals) + "PPG " + str(self.shorthanded_goals) + "SHG " + str(self.shots) + "SOG " + str(self.hits) + "H " + str(self.blocks) + "B " + str(self.fantasy_score) + "FS"

    __repr__ = __str__

dataset_dictionary = {}

for season in range(2008, 2023):
    season_dictionary = {}

    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '../res/moneypuck/moneypuck_' + str(season) + '-' + str((season + 1))[-2:] + '.csv')
 
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            # create dictionary entry
            id = int(row[0])
            if id not in season_dictionary:
                season_dictionary[id] = Player(id=id)

            # all situations
            if (row[5] == 'all'):
                season_dictionary[id].season = int(row[1])
                season_dictionary[id].name = str(row[2])
                season_dictionary[id].team = str(row[3])
                if str(row[4]) == 'L' or str(row[4]) == 'R':
                    season_dictionary[id].position = 'W'
                else:
                    season_dictionary[id].position = str(row[4])
                season_dictionary[id].games_played = float(row[6])
                season_dictionary[id].goals = float(row[34])
                season_dictionary[id].assists = float(row[27])+float(row[28])
                season_dictionary[id].points = float(row[33])
                season_dictionary[id].expected_goals = float(row[18])
                season_dictionary[id].shots = float(row[29])
                season_dictionary[id].hits = float(row[46])
                season_dictionary[id].blocks = float(row[83])

            # powerplay (5on4 only)
            elif (row[5] == '5on4'):
                season_dictionary[id].powerplay_goals = float(row[34])

            # shorthanded (4on5 only)
            elif (row[5] == '4on5'):
                season_dictionary[id].shorthanded_goals = float(row[34])

            # all other situations (5on3, 6on5, 3on3, etc.)
            elif (row[5] == 'other'):
                season_dictionary[id].special_goals = float(row[34])

        dataset_dictionary[season] = season_dictionary
        #pprint.pprint(season_dictionary)

#pprint.pprint(dataset_dictionary)

# to access a player for a specific season (season = str, id = int):
# dataset_dictionary['season'][id]
# pprint.pprint(dataset_dictionary['2022-23'][8478402])