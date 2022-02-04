from turtle import position
import pandas as pd

class Quadrant:
    radio_position = ""
    def __init__(self,name,station_order):
        self.name = name
        self.station_order = station_order
    def __str__(self):
        return '\nQuadrant: ' + self.name + '\nRadio Position: ' + self.radio_position + '\nStation Order: ' + str(self.station_order)
    def add_radio_position(self):
        if self.name[0:2] == 'BA':
            self.radio_position = "TAC_1"
        if self.name[0:2] in ['DF', 'PA', 'LF', 'BF', 'EF']:
            self.radio_position = "TAC_7"
        if self.name[0:2] in ['MF']:
            self.radio_position = "TAC_5"


station_order = pd.read_csv(r'C:\Users\cgass\OneDrive\Documents\Quadrant Station Order 2021-09-09.csv', names=['Quadrant','Station Order'], index_col= 0).to_dict()

new_station_order = station_order['Station Order']

quadrant_list = []

def create_quadrant_objects():
    for quadrant, sta_order in new_station_order.items():
        split_list = new_station_order[quadrant].split(",")
        quadrantx = Quadrant(quadrant, split_list)
        quadrant_list.append(quadrantx)
    return quadrant_list

def assign_radio_positions():
    for quadrant in quadrant_list:
        quadrant.add_radio_position()

create_quadrant_objects()
assign_radio_positions()

def get_station_order(grid):
    for quadrant in quadrant_list:
        if quadrant.name == grid:
            result = quadrant.station_order
        else:
            result = "Error: No station order exists for the specified quadrant"
        return result

print(get_station_order('DF013'))
