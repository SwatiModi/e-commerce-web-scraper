import pandas as pd
import argparse

# add argument parser for name of the csv
parser = argparse.ArgumentParser()
parser.add_argument('--name', help='Name of the CSV', action='store', dest='name')
args = parser.parse_args()

name = str(args.name)

df = pd.DataFrame()

df.to_csv( name + '.csv', index = False)