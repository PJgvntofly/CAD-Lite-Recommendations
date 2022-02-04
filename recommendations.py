import mysql.connector
from mysql.connector import Error
import pandas as pd
import create_server_connection
import units

#need to build out the full list of which quadrants are associated with which dispatch positions. Can be done by using csv functions from pandas.
position = {
    'TAC_1':['BA0001', 'BA0002', 'BA0003', 'BA0004'],
    'TAC_7':['DF009', 'DF010', 'DF011', 'DF013', 'DF055']
}

TAC_1 = {
    'BLS':[['Aid Unit', 'Engine', 'Ladder']],
    'BLSN':[['Aid Unit', 'Engine', 'Ladder']],
    'MED':['Medic Unit', 'Engine'],
    'MEDX':['Medic Unit', ['Engine', 'Ladder'], ['Engine', 'Ladder'], 'Medical Services Officer'],
    'HZ':[['Engine','Ladder'], 'Engine', 'Command Unit'],
    'FCC':['Engine', 'Engine', 'Ladder', 'Engine', 'Engine', 'Medic Unit', ['Aid Unit', 'Medic Unit'], 'Ladder', 'Command Unit', 'Medical Services Officer']
}

TAC_7 = {
    'BLS':[['Aid Unit', 'Medic Unit', 'Engine', 'Ladder']],
    'GLO':[['Engine', 'Ladder'], 'Engine']
}

station_order = {
    'BA0001':['STA 2', 'STA 3', 'STA 1', 'STA 5', 'STA 4', 'STA 6', 'STA 7', 'STA 61', 'STA 63', 'STA 82'],
    'BA0002':['STA 2', 'STA 3', 'STA 1', 'STA 5', 'STA 4', 'STA 6', 'STA 7', 'STA 61', 'STA 63', 'STA 82'],
    'DF009':['STA 19', 'KC STA 63', 'KC STA 57', 'STA 18', 'STA 20', 'KC STA 64', 'KC STA 65', 'STA 15'],
    'DF013':['KC STA 44', 'STA 18', 'KC STA 57', 'KC STA 51', 'STA 22', 'STA 19', 'KC STA 45', 'KC STA 63']
}

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
    units.refresh_units()
    if radio_position == 'TAC_1':
        radio_position = TAC_1
    if radio_position == 'TAC_7':
        radio_position = TAC_7
    response_plan = radio_position[call_type]
    rec_station_order = station_order[grid]
    if i <= len(response_plan):
        for unit_type in response_plan:
            list_result = False
            if isinstance(unit_type, list) == True:
                for option in unit_type:
                    if list_result == False:
                        for station in rec_station_order:
                            station_rank[station] = 1 + len(station_rank)
                            for unit in units.unit_list:
                                if unit.unit_number not in result and unit.unit_type == option and unit.unit_station == station and i < len(response_plan) and unit.unit_status in ['Available', 'AIQ']:
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
                                                unit_options = []
                                                unit_rank = {}
                                                sorted_units = {}
                                                sorted_unit_list = []
                    else:
                        list_result = False
                        continue                               
            else:
                for station in rec_station_order:
                    for unit in units.unit_list:
                        if unit.unit_type == unit_type and unit.unit_station == station and unit.unit_number not in result and i < len(response_plan) and unit.unit_status in ['Available', 'AIQ']:
                            if list_result == False:
                                result.append(unit.unit_number)
                                i += 1
                                list_result = True
    else:
        return result
    return f"{call_type}: {result}"

print(recommendations('bls','BA0002'))
print(recommendations('medX','BA0001'))
print(recommendations('FCC', 'BA0001'))
print(recommendations('bls', 'DF009'))
print(recommendations('GLO', 'DF013'))
