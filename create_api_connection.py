import requests
import json
from types import SimpleNamespace

def create_api_connection(url, organization_id, jurisdiction):
    response = None
    parameters = {
        'organizationId':organization_id,
        'jurisdiction':jurisdiction
    }
    try:
        response = requests.get(url, params=parameters)
        print("CAD Lite Database connection successful")
    except:
        print(f"Error: {response.status_code}")
    return response

class Unit:
    def __init__(self, unit_number, unit_type, unit_station, unit_status):
        self.unit_number = unit_number
        self.unit_type = unit_type
        self.unit_station = unit_station
        self.unit_status = unit_status
    def __str__(self):
        return '\nUnit Number: ' + self.unit_number + '\nUnit Type: ' + self.unit_type + '\nAssigned Station: ' + self.unit_station + '\nUnit Status: ' + self.unit_status

response = create_api_connection('https://uacy6ocd51.execute-api.us-west-2.amazonaws.com/prod/api/units/get-public', 1, 'WA').json()
unit_list = []
for unit in response['data']:
    unitx = Unit(unit['unitId'], unit['unitType'], unit['assignedStation'], unit['unitStatus'])
    unit_list.append(unitx)

