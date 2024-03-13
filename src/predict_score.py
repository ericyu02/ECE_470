#Predict future season's scores based off previous seasons stats
from dataset import dataset_dictionary, Player


def predict(season, id):
    last_season = str(season-1) + '-' + str((season))[-2:]

    predicted_stats = Player(id=id)
    predicted_stats.season = str(int(season)) + '-' + str((int(season) + 1))[-2:]
    predicted_stats.name = dataset_dictionary[last_season][id].name
    predicted_stats.team = dataset_dictionary[last_season][id].team
    predicted_stats.position = dataset_dictionary[last_season][id].position

    for prev_seasons in range(season-3, season):
        prev_season = str(prev_seasons) + '-' + str((prev_seasons + 1))[-2:]
        #grab data from dataset
        predicted_stats.games_played += dataset_dictionary[prev_season][id].games_played / 3
        predicted_stats.goals += dataset_dictionary[prev_season][id].goals / 3
        predicted_stats.assists += dataset_dictionary[prev_season][id].assists / 3
        predicted_stats.points += dataset_dictionary[prev_season][id].points / 3
        predicted_stats.powerplay_goals += dataset_dictionary[prev_season][id].powerplay_goals / 3
        predicted_stats.shorthanded_goals += dataset_dictionary[prev_season][id].shorthanded_goals / 3
        predicted_stats.special_goals += dataset_dictionary[prev_season][id].special_goals / 3
        predicted_stats.shots += dataset_dictionary[prev_season][id].shots / 3
        predicted_stats.hits += dataset_dictionary[prev_season][id].hits / 3
        predicted_stats.blocks += dataset_dictionary[prev_season][id].blocks / 3

    return predicted_stats