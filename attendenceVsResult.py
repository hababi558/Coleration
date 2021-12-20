import numpy as np
import csv
import plotly.express as px

def getDataSource(data_path):
    mark = []
    attendance = []
    
    with open(data_path) as csv_file:
        csvReader=csv.DictReader(csv_file)
        for row in csvReader:
            mark.append(float(row['Marks In Percentage']))
            attendance.append(float(row['Days Present']))
    return {'x':mark,'y':attendance}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print("correlation between Attendance and marks",correlation[0,1])

def setup():
    data_path = 'Marks.csv'
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()  