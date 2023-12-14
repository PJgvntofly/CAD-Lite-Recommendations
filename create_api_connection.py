import requests
from urllib3.exceptions import InsecureRequestWarning
from log_config import connection_log
import PySimpleGUI as sg


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#Creates a popup window roughly centered in the main window showing that the API connection is in process
def create_loading_window(window):
    main_window_location = window.current_location()
    text = 'CAD Lite Recommendations Loading...'
    popup_size = (len(text), 10)
    popup_x = (main_window_location[0] + window.size[0] // 2) - popup_size[0] // 2
    popup_y = (main_window_location[1] + window.size[1] // 2) - popup_size[1]

    sg.popup_no_buttons(text, location=(popup_x, popup_y), no_titlebar=True,non_blocking=True,auto_close_duration=.1, auto_close=True, keep_on_top=True)

#Creates an API connection with a popup showing that the connection is in process
def create_api_connection(url, organization_id, jurisdiction, window):
    response = None
    parameters = {
        'organizationId':organization_id,
        'jurisdiction':jurisdiction
    }
    connection_log.info('Attempting API connection')
    create_loading_window(window)

    try:
        response = requests.get(url, params=parameters, verify=False)
        connection_log.info(f"Verbose connection successful. Status code: {response.status_code}")
        print("CAD Lite Database connection successful")
    except Exception as e:
        connection_log.exception(f"An error occured while establishing the API connection - {e}")
        print(f"Error connecting to CAD Lite Database")
        response = False
    return response