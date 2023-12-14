from multiprocessing.connection import wait
from recommendations import get_radio, recommendations
import offline_mode
from import_response_plans import import_response_plans
from log_config import connection_log
from log_config import rec_log

def get_recommendations(call_type, grid, window):
    #Function to take inputs for the call type and grid from the GUI and execute the recommendaitons function
    unconfirmed_fire_types = set(['FR', 'FC'])
    rec_log.info("\nStarting new recommendation cycle")
    
    #Get response plans to determine if the entered call type is valid
    response_plans = import_response_plans()
    rec_log.debug(f"SNO911 Response Plan Keys: {response_plans['SNO911'].keys()}")

    #Check to see if inputs were provided 
    try:
        rec_log.debug(f"Input Call Type: {call_type}")
        rec_log.debug(f"Input Fire Grid: {grid}")
        grid = grid.strip().upper()
        call_type = call_type.strip().upper()

        if call_type in unconfirmed_fire_types:
            print(f"Using {call_type}C plan")
            call_type = call_type + 'C'

    #Handle errors with the provided inputs
    except ValueError as error:
        rec_log.error(f'An error occured while getting recommendations {error}')
    
    if get_radio(grid):
        if call_type in response_plans['SNO911']['TAC-1']:
            try:
                #Try to obtain recommendations through the API connection
                return recommendations(call_type,grid, window)
            except Exception as e:
                #If there is an error with the API connection, log the exception and try offline mode
                connection_log.exception(f"Error during recommendations - {e}")
                return offline_mode.offline_recommendations(call_type,grid, window)
        else:
            rec_log.warning(f"Invalid call type entered: {call_type}")
            print(f"{call_type} is not valid. \nPlease enter a valid call type \n")
    else:
        rec_log.warning(f"Invalid grid entered: {grid}")
        print(f'{grid} is not valid. \nPlease enter a valid fire grid \n')


