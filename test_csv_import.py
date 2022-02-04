import csv
import pandas as pd

station_order = {}
f = open(r"C:\Users\cgass\OneDrive\Documents\Quadrant Station Order 2021-09-09.csv")
csv_f = csv.reader(f)
for row in csv_f:
    quadrant, order = row
    station_order[quadrant] = order.split(",")
f.close()

def create_positions():
    position = {
        'TAC_1':[],
        'TAC_3':[],
        'TAC_5':[],
        'TAC_7':[]
    }
    for quadrant in station_order.keys():
        if quadrant[:2] == 'BA':
            position['TAC_1'].append(quadrant)
        if quadrant[:2] in ['DF', 'LF', 'BF', 'EF']:
            position['TAC_7'].append(quadrant)
        if quadrant[:2] in ['MF']:
            position['TAC_5'].append(quadrant)
    return position

