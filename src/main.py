import argparse
import csv
import os
import pprint
import numpy as np

from dataset import dataset_dictionary
from predict_score import predict_player, predict_season

parser = argparse.ArgumentParser()
parser.add_argument('season', help="season to predict (i.e. 2022-23)")
parser.add_argument('id', help="id of player / 'all'", type=str)
args = parser.parse_args()

season = int(args.season.split("-")[0])

# Player    id
# McDavid   8478402
# Matthews  8479318
# Makar     8480069
# Trocheck  8476389

# For data analysis, remove for final submission
if args.id == 'test':
    accuracy = []
    for season in range(2009, season + 1):
        ranking, mpd = predict_season(season)
        #pprint.pprint(ranking)
        if mpd is not None:
            print(str(season) + '-' + str(season + 1)[-2:] + ': Accuracy = {:.1%}'.format(1-mpd))
            accuracy.append(1-mpd)
    print('Average = {:.1%}'.format(np.mean(accuracy)))
# ---------------------------

elif args.id == 'all':
    ranking, mpd = predict_season(season)
    pprint.pprint(ranking)
    if mpd is not None:
        print('Accuracy = {:.1%}'.format(1-mpd))
else:
    ranking, pd = predict_player(season, int(args.id))
    pprint.pprint(ranking)
    if pd is not None:
        print('Accuracy = {:.1%}'.format(1-pd))