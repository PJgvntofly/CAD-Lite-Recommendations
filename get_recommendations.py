from multiprocessing.connection import wait
from recommendations import get_radio, recommendations
import offline_mode
from import_response_plans import import_response_plans
from log_config import connection_log
from log_config import rec_log

def get_recommendations(call_type, grid):
    rec_log.info("\nStarting new recommendation cycle")
    response_plans = import_response_plans()
    rec_log.debug(f"SNO911 Response Plan Keys: {response_plans['SNO911'].keys()}")
    try:
        #call_type = input("Enter the call type:")
        rec_log.debug(f"Input Call Type: {call_type}")
        #grid = input("Enter the fire grid:")
        rec_log.debug(f"Input Fire Grid: {grid}")
        grid = grid.strip().upper()
        call_type = call_type.strip().upper()
        if call_type == 'FR':
            print("Using FRC plan")
            call_type = 'FRC'
        if call_type == 'FC':
            print('Using FCC plan')
            call_type = 'FCC'
    except KeyboardInterrupt:
        rec_log.error('User pressed ctrl+c')
    if get_radio(grid):
        if call_type in response_plans['SNO911']['TAC-1']:
            try:
                return recommendations(call_type,grid)
            except Exception:
                connection_log.exception("")
                return offline_mode.offline_recommendations(call_type,grid)
        else:
            rec_log.warning(f"Invalid call type entered: {call_type}")
            print(f"{call_type} is not valid. \nPlease enter a valid call type \n")
    else:
        rec_log.warning(f"Invalid grid entered: {grid}")
        print(f'{grid} is not valid. \nPlease enter a valid fire grid \n')
    #get_recommendations()

#get_recommendations()