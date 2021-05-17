import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
     days_Present = []
     marks = []
     with open(data_path) as csv_file:
          csv_reader = csv.DictReader(csv_file)
          for row in csv_reader:
               days_Present.append(float(row["Days Present"]))
               marks.append(float(row["Marks In Percentage"]))
     return {"x": days_Present, "y": marks}

def findCorrelation(dataSource):
     correlation = np.corrcoef(dataSource["x"],dataSource["y"])
     print('Days Present vs Marks In Percentage: \n',correlation[0,1])

def setup():
     data_path = 'school.csv'
     dataSource = getDataSource(data_path)
     findCorrelation(dataSource)

setup()