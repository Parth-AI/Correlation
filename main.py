import csv
import plotly.express as px

with open('tv.csv') as tv:
     data = csv.DictReader(tv)
     show1 = px.scatter(data, x='Size of TV', y='Average time spent watching TV in a week (hours)', title="TV Watch Time")
show1.show()