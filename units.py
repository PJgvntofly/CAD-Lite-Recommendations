import create_api_connection
import csv
import logging

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
    connection = create_api_connection.create_api_connection('https://uacy6ocd51.execute-api.us-west-2.amazonaws.com/prod/api/units/get-public', 1, 'WA')
    return connection

def silent_connection():
    connection = create_api_connection.silent_api_connection('https://uacy6ocd51.execute-api.us-west-2.amazonaws.com/prod/api/units/get-public', 1, 'WA')
    return connection

def refresh_units():
    unit_list = []
    connection = create_connection()
    try:
        logging.info("Refreshing units")
        response = connection.json()
        for unit in response['data']:
            unitx = Unit(unit['unitId'], unit['unitType'], unit['assignedStation'], unit['unitStatus'], unit['crossStaffing'])
            unit_list.append(unitx)
        for unit in unit_list:
            if unit.cross_staffing is not None:
                unit.cross_staffing = unit.cross_staffing.split("-")
        connection.close()
    except Exception:
        logging.exception()
        unit_list = import_units()
    return unit_list

def import_units():
    unit_list = []
    print('Starting Offline Mode')
    try:
        logging.info("Importing offline units")
        f = open(r'.\CADLiteUnitList.csv','r', newline='')
        csv_f = csv.reader(f)
        for row in csv_f:
            unit_number, jurisdiction, unit_type, assigned_station, assigned_beat, display_in_usm, unit_status, cross_staffing = row
            unitx = Unit(unit_number, unit_type, assigned_station, unit_status, cross_staffing)
            unit_list.append(unitx)
        f.close()
        for unit in unit_list:
            unit.unit_status = 'AIQ'
            unit.cross_staffing = unit.cross_staffing.split("-")
        logging.info("Finished importing offline units")
        return unit_list
    except Exception:
        logging.exception("")
        print("Error importing offline unit list")
        return unit_list
    
