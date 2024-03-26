import argparse
import csv
import os
import pprint

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

if args.id == 'all':
    pprint.pprint(predict_season(season))
else:
    pprint.pprint(predict_player(season, int(args.id)))

# TODO calculate average percentage difference between predicted score and real score