from dataset import dataset_dictionary, Player, pprint

def predict(season, id):
    
    # add all player entries from dataset dictionary to player dictionary
    player_dictionary = {}
    for temp_season, temp_entry in dataset_dictionary.items():
        if id in temp_entry:
            player_dictionary[temp_season] = temp_entry[id]
    #pprint.pprint(player_dictionary)
    
    # figure out range of seasons to use based on games played
    season_range = 0
    games_played = 0
    threshold_games_played = 200
    # if player has played less than 3 years, use full dataset
    if len(player_dictionary) < 3:
        season_range = len(player_dictionary)
    # else use dataset until player has enough (200) games played
    else:
        while games_played < threshold_games_played:
            season_range += 1
            games_played += player_dictionary[season - season_range].games_played
    
    # predict player stats 
    predicted_stats = Player(id=id)
    predicted_stats.season = season
    predicted_stats.name = dataset_dictionary[season - 1][id].name
    predicted_stats.team = dataset_dictionary[season - 1][id].team
    predicted_stats.position = dataset_dictionary[season - 1][id].position

    for prev_season in range(season - season_range, season):
        print(prev_season)
        # grab data from dataset
        predicted_stats.games_played += dataset_dictionary[prev_season][id].games_played / season_range
        predicted_stats.goals += dataset_dictionary[prev_season][id].goals / season_range
        predicted_stats.assists += dataset_dictionary[prev_season][id].assists / season_range
        predicted_stats.points += dataset_dictionary[prev_season][id].points / season_range
        predicted_stats.powerplay_goals += dataset_dictionary[prev_season][id].powerplay_goals / season_range
        predicted_stats.shorthanded_goals += dataset_dictionary[prev_season][id].shorthanded_goals / season_range
        predicted_stats.special_goals += dataset_dictionary[prev_season][id].special_goals / season_range
        predicted_stats.shots += dataset_dictionary[prev_season][id].shots / season_range
        predicted_stats.hits += dataset_dictionary[prev_season][id].hits / season_range
        predicted_stats.blocks += dataset_dictionary[prev_season][id].blocks / season_range

    return predicted_stats