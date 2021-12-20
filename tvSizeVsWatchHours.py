import numpy as np
import csv
import plotly.express as px

def getDataSource(data_path):
    sizeOfTv = []
    averageTimeSpent = []
    
    with open(data_path) as csv_file:
        csvReader=csv.DictReader(csv_file)
        for row in csvReader:
            sizeOfTv.append(float(row['Size of TV']))
            averageTimeSpent.append(float(row['Average time spent watching TV in a week (hours)']))
    return {'x':sizeOfTv,'y':averageTimeSpent}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print("Correlation between Size of Tv vs Average time spent watching TV in a week (hours)",correlation[0,1])

def setup():
    data_path = 'tv.csv'
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()  