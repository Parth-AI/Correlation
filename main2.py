import csv
import plotly.express as px

with open('school.csv') as tv:
     data = csv.DictReader(tv)
     show1 = px.scatter(data, x='Days Present', y='Marks In Percentage', title="Percentage")
show1.show()