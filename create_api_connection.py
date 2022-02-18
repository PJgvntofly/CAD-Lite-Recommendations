from unicodedata import category
import requests
from urllib3.exceptions import InsecureRequestWarning
from datetime import datetime
import logging

logging.basicConfig(filename=f'./logs/{datetime.today().strftime("%m %d")} application_log.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', encoding='utf-8', level=logging.DEBUG)

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def create_api_connection(url, organization_id, jurisdiction):
    response = None
    parameters = {
        'organizationId':organization_id,
        'jurisdiction':jurisdiction
    }
    try:
        response = requests.get(url, params=parameters, verify=False)
        logging.info(f"Verbose connection successful. Status code: {response.status_code}")
        print("CAD Lite Database connection successful")
    except:
        logging.exception("")
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
        logging.info(f"Silent connection successful. Status code: {response.status_code}")
    except:
        logging.exception("")
        print(f"Error connecting to CAD Lite Database")
    return response