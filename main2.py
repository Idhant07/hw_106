import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    coffee_in_ml=[]
    sleeping_hours=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
             coffee_in_ml.append(float(row["Coffee in ml"]))         
             sleeping_hours.append(float(row["sleep in hours"])) 
    return {"x" : coffee_in_ml, "y": sleeping_hours}        
    
def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"], data_source["y"])
    print(correlation)

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df, x="Coffee in ml", y="sleep in hours")
        fig.show()

def setup():
    data_path = "coffee_data.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()