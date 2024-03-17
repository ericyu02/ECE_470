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
        
        # normalize each stat by games played per season
        gp = dataset_dictionary[prev_season][id].games_played
        g = dataset_dictionary[prev_season][id].goals / gp
        xg = dataset_dictionary[prev_season][id].expected_goals / gp

        a = dataset_dictionary[prev_season][id].assists / gp
        
        ppg = dataset_dictionary[prev_season][id].powerplay_goals / gp
        shg = dataset_dictionary[prev_season][id].shorthanded_goals / gp
        special_g = dataset_dictionary[prev_season][id].special_goals / gp

        s = dataset_dictionary[prev_season][id].shots / gp
        h = dataset_dictionary[prev_season][id].hits / gp
        b = dataset_dictionary[prev_season][id].blocks / gp

        # TODO decide on best weights for expected and special goals
        predicted_stats.games_played = 82
        predicted_stats.goals += (g + ((xg - g)*0.2) + (special_g*0.5)) * 82/season_range
        predicted_stats.assists += (a) * 82/season_range
        predicted_stats.points += (g + a) * 82/season_range
        predicted_stats.powerplay_goals += (ppg + (special_g*0.4)) * 82/season_range
        predicted_stats.shorthanded_goals += (shg + (special_g*0.1)) * 82/season_range
        predicted_stats.shots += (s) * 82/season_range
        predicted_stats.hits += (h) * 82/season_range
        predicted_stats.blocks += (b) * 82/season_range

    return predicted_stats