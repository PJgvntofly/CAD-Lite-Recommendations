import mysql.connector
from mysql.connector import Error
import create_server_connection
import csv

class Unit:
    def __init__(self, unit_number, unit_type, unit_station, unit_status, cross_staffing):
        self.unit_number = unit_number
        self.unit_type = unit_type
        self.unit_station = unit_station
        self.unit_status = unit_status
        self.cross_staffing = cross_staffing
    def __str__(self):
        return '\nUnit Number: ' + self.unit_number + '\nUnit Type: ' + self.unit_type + '\nAssigned Station: ' + self.unit_station + '\nUnit Status: ' + self.unit_status + '\nCross Staffing: ' +self.cross_staffing

def create_connection():
    connection = create_server_connection.create_server_connection('localhost', 'recommendations','testpassword1','cad_lite')
    return connection

def silent_connection():
    connection = create_server_connection.silent_server_connection('localhost', 'recommendations','testpassword1','cad_lite')
    return connection
    
q1 = """
SELECT
unit_number,
unit_type,
assigned_station,
unit_status,
cross_staffing
FROM
units
WHERE
jurisdiction NOT LIKE "WA%"
"""

def refresh_units():
    unit_list = []
    connection = create_connection()
    if connection != None:
        results = create_server_connection.read_query(connection, q1)
        for unit_number, unit_type, assigned_station, unit_status, cross_staffing in results:
            unitx = Unit(unit_number, unit_type, assigned_station, unit_status, cross_staffing)
            unit_list.append(unitx)
            connection.close()
    else:
        unit_list = import_units()
    for unit in unit_list:
        unit.cross_staffing = unit.cross_staffing.split("-")
    return unit_list

def import_units():
    unit_list = []
    print('Failed to connect to CAD Lite Database \nStarting Offline Mode')
    f = open(r'C:\Users\cgass\OneDrive\Documents\CAD Lite\CADLiteUnitList_2021-04-16.csv','r', newline='')
    csv_f = csv.reader(f)
    for row in csv_f:
        unit_number, jurisdiction, unit_type, assigned_station, assigned_beat, display_in_usm, unit_status, cross_staffing = row
        unitx = Unit(unit_number, unit_type, assigned_station, unit_status, cross_staffing)
        unit_list.append(unitx)
    f.close()
    for unit in unit_list:
        unit.unit_status = 'AIQ'
        unit.cross_staffing = unit.cross_staffing.split("-")
    return unit_list

refresh_units()
