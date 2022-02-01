import mysql.connector
from mysql.connector import Error
import pandas as pd
import create_server_connection

connection = create_server_connection.create_server_connection('localhost', 'root','testpassword1','cad_lite')

position = {
    'TAC_1':['BA0001', 'BA0002', 'BA0003', 'BA0004'],
    'TAC_7':['DF009', 'DF010', 'DF011', 'DF013', 'DF055']
}

TAC_1 = {
    'BLS':[['Aid Unit', 'Engine', 'Ladder']],
    'BLSN':[['Aid Unit', 'Engine', 'Ladder']],
    'MED':['Medic Unit', 'Engine'],
    'MEDX':['Medic Unit', ['Engine', 'Ladder'], ['Engine', 'Ladder'], 'Medical Services Officer'],
    'HZ':[['Engine','Ladder'], 'Engine', 'Command Unit']
}

station_order = {
    'BA0001':['STA 2', 'STA 3', 'STA 1', 'STA 5', 'STA 4', 'STA 6', 'STA 7', 'STA 61', 'STA 63', 'STA 82'],
    'BA0002':['STA 2', 'STA 3', 'STA 1', 'STA 5', 'STA 4', 'STA 6', 'STA 7', 'STA 61', 'STA 63', 'STA 82']
}

class Unit:
    def __init__(self, unit_number, unit_type, unit_station, unit_status):
        self.unit_number = unit_number
        self.unit_type = unit_type
        self.unit_station = unit_station
        self.unit_status = unit_status
    def __str__(self):
        return '\nUnit Number: ' + self.unit_number + '\nUnit Type: ' + self.unit_type + '\nAssigned Station: ' + self.unit_station + '\nUnit Status: ' + self.unit_status

q1 = """
SELECT
unit_number,
unit_type,
assigned_station,
unit_status
FROM
units
"""
results = create_server_connection.read_query(connection, q1)

unit_list = []

def refresh_units():
    for unit_number, unit_type, assigned_station, unit_status in results:
        unitx = Unit(unit_number, unit_type, assigned_station, unit_status)
        unit_list.append(unitx)

def get_radio(val):
    for key, values in position.items():
        if val in values:
            return key

def recommendations(call_type,grid):
    call_type = call_type.strip().upper()
    grid = grid.strip().upper()
    result = []
    list_result = False
    i = 0
    station_rank = {}
    unit_options = []
    unit_rank = {}
    sorted_units = {}
    sorted_unit_list = []
    radio_position = get_radio(grid)
    refresh_units()
    if radio_position == 'TAC_1':
        radio_position = TAC_1
    response_plan = radio_position[call_type]
    rec_station_order = station_order[grid]
    if i <= len(response_plan):
        for unit_type in response_plan:
            if isinstance(unit_type, list) == True:
                for option in unit_type:
                    if list_result == False:
                        for station in rec_station_order:
                            station_rank[station] = 1 + len(station_rank)
                            for unit in unit_list:
                                if unit.unit_type == option and unit.unit_station == station and unit.unit_number not in result and i < len(response_plan) and unit.unit_status in ['Available', 'AIQ']:
                                    unit_options.append(unit)
                                    for unit in unit_options:
                                        if list_result == False:
                                            unit_rank[unit.unit_number] = station_rank[unit.unit_station]
                                            sorted_units = sorted(unit_rank.items(), key=lambda x: x[1])
                                            for apparatus, station_r in sorted_units:
                                                sorted_unit_list.append(apparatus)
                                                result.append(sorted_unit_list[0])
                                                i += 1
                                                list_result = True
                    else:
                        list_result = False
                        continue                               
            else:
                for station in rec_station_order:
                    for unit in unit_list:
                        if unit.unit_type == unit_type and unit.unit_station == station and unit.unit_number not in result and i < len(response_plan) and unit.unit_status in ['Available', 'AIQ']:
                            if list_result == False:
                                result.append(unit.unit_number)
                                i += 1
                                list_result = True
    else:
        return result
    return f"{call_type}: {result}"

print(recommendations('bls','BA0002'))
print(recommendations('medx','BA0001'))
print(recommendations('Hz', 'BA0001'))
