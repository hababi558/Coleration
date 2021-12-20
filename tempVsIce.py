import numpy as np
import csv
import plotly.express as px

def getDataSource(data_path):
    icecreamSales = []
    coldDrinkSales = []
    
    with open(data_path) as csv_file:
        csvReader=csv.DictReader(csv_file)
        for row in csvReader:
            icecreamSales.append(float(row['Temperature']))
            coldDrinkSales.append(float(row['Ice-cream Sales']))
    return {'x':icecreamSales,'y':coldDrinkSales}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print("correlation between \n Temperature vs Icecream sales",correlation[0,1])

def setup():
    data_path = 'Temperature.csv'
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()  