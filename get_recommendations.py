from multiprocessing.connection import wait
import recommendations
import offline_mode
import logging

def get_recommendations():
    call_type = input("Enter the call type:")
    grid = input("Enter the fire grid:")
    grid = grid.strip().upper()
    call_type = call_type.strip().upper()
    if recommendations.get_radio(grid):
        if call_type in recommendations.TAC_1.keys():
            try:
                print(recommendations.recommendations(call_type,grid),'\n')
            except Exception:
                logging.exception("")
                print(offline_mode.offline_recommendations(call_type,grid),'\n')
        else:
            logging.debug(f"Invalid call type entered: {call_type}")
            print(f"{call_type} is not valid. \nPlease enter a valid call type \n")
    else:
        logging.debug(f"Invalid grid entered: {grid}")
        print(f'{grid} is not valid. \nPlease enter a valid fire grid \n')
    get_recommendations()

get_recommendations()