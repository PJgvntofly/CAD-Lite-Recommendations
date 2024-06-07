import create_api_connection
import csv
from log_config import connection_log, rec_log
import regex as re

#Constants
API_URL = 'https://Zuacy6ocd51.execute-api.us-west-2.amazonaws.com/prod/api/units/get-public'
OFFLINE_CSV_PATH = r'.\CADLiteUnitList.csv'

#Create a class to represent a unit
class Unit:
    def __init__(self, unit_number, unit_type, unit_station, unit_status, cross_staffing):
        #Constructor initializes unit attributes
        self.unit_number = unit_number
        self.unit_type = unit_type
        self.unit_station = unit_station
        self.unit_status = unit_status
        self.cross_staffing = cross_staffing
    def __str__(self):
        #String representation of a unit for easier debugging
        return '\nUnit Number: ' + self.unit_number + '\nUnit Type: ' + self.unit_type + '\nAssigned Station: ' + self.unit_station + '\nUnit Status: ' + self.unit_status + '\nCross Staffing: ' +self.cross_staffing

def create_connection(window):
    #Function to create an API connection with output
    connection = create_api_connection.create_api_connection(API_URL, 1, 'WA', window)
    return connection

def refresh_units(window):
    #Function to refresh unit data from the API
    unit_list = []
    try:
        connection_log.info("Refreshing units")
        with create_connection(window) as connection:
            response = connection.json()
            #Create Unit objects from API response
            unit_list = [Unit(unit['unitId'], unit['unitType'], unit['assignedStation'], unit['unitStatus'], unit['crossStaffing']) for unit in response['data']]
            for unit in unit_list:
                #Use regex to get the generic unit type from ALS units. i.e. changing ALS Engine to Engine
                pattern = r'ALS (\w+)'
                match = re.match(pattern, unit.unit_type)
                if match:
                    unit.unit_type = match[1]
                #Split cross-staffing string into a list
                if unit.cross_staffing is not None:
                    unit.cross_staffing = unit.cross_staffing.split("-")

    except Exception:
        connection_log.exception("An error occurred while refreshing units")
        unit_list = None
    return unit_list

def import_units():
    #Function to import units from the .csv file should the app be unable to connect to the API
    unit_list = []
    print('Starting Offline Mode')
    try:
        connection_log.info("Importing offline units")
        with open(OFFLINE_CSV_PATH,'r', newline='') as f:
            csv_f = csv.reader(f)
            unit_list = [Unit(row[0], row[2], row[3], 'AIQ', row[7].split("-")) for row in csv_f if row != '']
        connection_log.info("Finished importing offline units")
    except FileNotFoundError:
        connection_log.error("Error importing offline unit list: CSV file not found")
    except Exception:
        connection_log.error("Error importing offline unit list")
    return unit_list
    
