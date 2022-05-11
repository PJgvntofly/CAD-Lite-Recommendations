import requests
from urllib3.exceptions import InsecureRequestWarning
from log_config import connection_log

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def create_api_connection(url, organization_id, jurisdiction):
    response = None
    parameters = {
        'organizationId':organization_id,
        'jurisdiction':jurisdiction
    }
    try:
        response = requests.get(url, params=parameters, verify=False)
        connection_log.info(f"Verbose connection successful. Status code: {response.status_code}")
        print("CAD Lite Database connection successful")
    except:
        connection_log.exception("")
        print(f"Error connecting to CAD Lite Database")
    return response

def silent_api_connection(url, organization_id, jurisdiction, verify=False):
    response = None
    parameters = {
        'organizationId':organization_id,
        'jurisdiction':jurisdiction
    }
    try:
        response = requests.get(url, params=parameters)
        connection_log.info(f"Silent connection successful. Status code: {response.status_code}")
    except:
        connection_log.exception("")
        print(f"Error connecting to CAD Lite Database")
    return response