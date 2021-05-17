import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
     tvSize = []
     tvWatchtime = []
     with open(data_path) as csv_file:
          csv_reader = csv.DictReader(csv_file)
          for row in csv_reader:
               tvSize.append(float(row["Size of TV"]))
               tvWatchtime.append(float(row["Average time spent watching TV in a week (hours)"]))
     return {"x": tvSize, "y": tvWatchtime}

def findCorrelation(dataSource):
     correlation = np.corrcoef(dataSource["x"],dataSource["y"])
     print('Correlation between Size of TV vs Averrage Watch Time of TV: \n',correlation[0,1])

def setup():
     data_path = 'tv.csv'
     dataSource = getDataSource(data_path)
     findCorrelation(dataSource)

setup()