import requests

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
        print(f"Error connecting to CAD Lite Database")
    return response

def silent_api_connection(url, organization_id, jurisdiction):
    response = None
    parameters = {
        'organizationId':organization_id,
        'jurisdiction':jurisdiction
    }
    try:
        response = requests.get(url, params=parameters)
    except:
        print(f"Error connecting to CAD Lite Database")
    return response