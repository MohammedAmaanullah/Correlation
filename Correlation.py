from google.colab import files
a=files.upload()

import csv
import pandas as pd
import plotly.express as pe
import numpy
with open("Student Marks vs Days Present.csv") as x:
  df = csv.DictReader(x)
  fig = pe.scatter(df,x="Marks In Percentage", y="Days Present")
  fig.show()

def getDataSource(data_path):
  DP = []
  MIP = []
  with open(data_path) as csv:
    csv_reader = csv.DictReader(csv)
    for d in csv_reader:
      DP.append(float(i["Days Present"]))
      MIP.append(float(i["Marks In Percentage"]))
  return("x":Days Present, "y":Marks In Percentage)

def findingCorrelation(datasource):
  correlation = np.corrcoef(datasource["x"], datasource["y"])
  print("Correlation between Size of Tv and Average time spent watching Tv in a week;",correlation[0,1])

data_path  = "=Student Marks vs Days Present.csv"
datasource = getDataSource(data_path)
findingCorrelation(datasource) 