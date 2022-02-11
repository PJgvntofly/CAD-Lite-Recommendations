import mysql.connector
from mysql.connector import Error
import create_server_connection

class Unit:
    def __init__(self, unit_number, unit_type, unit_station, unit_status):
        self.unit_number = unit_number
        self.unit_type = unit_type
        self.unit_station = unit_station
        self.unit_status = unit_status
    def __str__(self):
        return '\nUnit Number: ' + self.unit_number + '\nUnit Type: ' + self.unit_type + '\nAssigned Station: ' + self.unit_station + '\nUnit Status: ' + self.unit_status

#update values passed to this function to the appropriate CAD Lite MySQL database
connection = create_server_connection.create_server_connection('localhost', 'recommendations','testpassword1','cad_lite')

q1 = """
SELECT
unit_number,
unit_type,
assigned_station,
unit_status
FROM
units
WHERE
jurisdiction NOT LIKE "WA%"
"""

def refresh_units():
    unit_list = []
    #update values passed to this function to the appropriate CAD Lite MySQL database
    connection = create_server_connection.create_server_connection('localhost', 'recommendations','testpassword1','cad_lite')
    results = create_server_connection.read_query(connection, q1)
    for unit_number, unit_type, assigned_station, unit_status in results:
        unitx = Unit(unit_number, unit_type, assigned_station, unit_status)
        unit_list.append(unitx)
    if connection.is_connected():
        connection.close()
    return unit_list
