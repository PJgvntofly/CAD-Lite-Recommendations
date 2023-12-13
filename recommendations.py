#Import necessary modules
import PySimpleGUI as sg
import units
import station_order
from log_config import rec_log, connection_log
from import_response_plans import import_response_plans

#Create station orders, positions, and import response plans
station_orders = station_order.create_station_order()
position = station_order.create_positions(station_orders)
fdid = position[1]
position = position[0]
frls = import_response_plans()

#Helper functions to get the radio positon and FDID based on the grid
def get_radio(grid):
    for key, values in position.items():
        if grid in values:
            return key

def get_fdid(grid):
    for key, values in fdid.items():
        if grid in values:
            return key

#Helper fuction to determine if the call is in a no-hydrant area
def find_hydrant(call, radio_position):
    if radio_position in ['TAC-3', 'TAC-5'] and call in ['FCC', 'FRC']:
        no_hydrant_response = False
        no_hydrant = ""
        while no_hydrant_response is False:
            no_hydrant = sg.popup_get_text('Is this call in a No Hydrant area? Enter Y for yes and N for no:',title='No Hydrant Area')
            if no_hydrant is None:
                no_hydrant = 'N'
            rec_log.debug(f"No Hydrant input: {no_hydrant}")
            no_hydrant = no_hydrant.strip().upper()
            no_hydrant = no_hydrant[0]
            if no_hydrant == "Y":
                no_hydrant_response = True
                return call + " - No Hydrant"
            if no_hydrant == 'N':
                return call
            if no_hydrant not in ['Y', 'N']:
                sg.popup('Please enter only Y or N')
    return call

#Function to retrieve the response plan based on the call type, grid, and department
def get_response_plan(call_type, grid, department):
    radio_position = get_radio(grid)

    #Determines if a No-Hydrant plan needs to be used
    call_type = find_hydrant(call_type, radio_position)

    if radio_position == None:
        return False

    if grid in station_orders:
        agency = 'SNO911'
    if grid in frls[agency].keys() and call_type in frls[agency][grid].keys():
        response_plan = frls[agency][grid][call_type]
    elif department in frls[agency].keys() and call_type in frls[agency][department].keys():
        response_plan = frls[agency][department][call_type]
    else:
        response_plan = frls[agency][radio_position][call_type]
    return response_plan

#Function to clean up the unit list by removing units with the 'Off Shift' status and police units with no assigned station
def clean_unit_list(unit_list):
    return [unit for unit in unit_list if unit.unit_status != 'Off Shift' and unit.unit_station != 'None']

#Function to generate recommendations based on the call type and grid
def recommendations(call_type,grid):
    rec_log.info("Beginning recommendations")
    call_type = call_type.strip().upper()
    grid = grid.strip().upper()
    result = []
    unfulfilled_resources = False
    unfulfilled = []
    list_result = False
    unit_options = []
    unit_rank = {}
    sorted_units = {}
    sorted_unit_list = []
    unit_list = []
    cross_staffing_list = []
    cross_staff_dict = {}
    sorted_unit_log = {}
    station_rank_log = {}

    #Inform users to use the second alarm type code for specific rescue call types
    if call_type in ['RESCS', 'RESTR']:
        return print("Use second alarm type code: {}".format(call_type + "2"))
    connection_log.info('Initializing database connection')
    unit_list = units.refresh_units()
    unit_list = clean_unit_list(unit_list)
    department = get_fdid(grid)
    response_plan = get_response_plan(call_type, grid, department)

    #If unable to determine a response plan, exit and advise the user that the quadrant isn't supported
    if response_plan is False:
        return print('Quadrant is not supported')
    rec_station_order = station_orders[grid]
    station_rank = {station: 1 + i for i, station in enumerate(rec_station_order)}
    response_plan_length = len(response_plan)

    for i, unit_type in enumerate(response_plan):
        list_result = False
        unit_options = []
        unit_rank = {}
        sorted_units = {}
        sorted_unit_list = []

        if isinstance(unit_type, list):
            unit_options = [unit for unit in unit_list if unit.unit_number not in result
                            and unit.unit_number not in cross_staffing_list
                            and unit.unit_type in unit_type
                            and unit.unit_station in rec_station_order
                            and i < response_plan_length
                            and unit.unit_status in ['Available', 'AIQ']]

        else:
            unit_options = [unit for unit in unit_list if unit.unit_type == unit_type
                            and unit.unit_station in rec_station_order
                            and unit.unit_number not in result
                            and unit.unit_number not in cross_staffing_list
                            and i < response_plan_length
                            and unit.unit_status in ['Available', 'AIQ']]

        for unit in unit_options:
            if not list_result:
                unit_rank[unit.unit_number] = station_rank[unit.unit_station]
            if unit.cross_staffing is not None:
                cross_staff_dict[unit.unit_number] = unit.cross_staffing
        
        sorted_units = sorted(unit_rank.items(), key=lambda x: x[1])
        sorted_unit_list = [apparatus for apparatus, station_r in sorted_units]

        for sorted_unit in sorted_unit_list:
            if not list_result: 
                result.append(sorted_unit)
                if sorted_unit in cross_staff_dict.keys():
                    cross_staffing_list.extend(cross_staff_dict[sorted_unit])
                sorted_unit_log[sorted_unit] = sorted_units
                station_rank_log[sorted_unit] = station_rank
                list_result = True

        if not list_result:
            unfulfilled_resources = True
            unfulfilled.append(unit_type)
    rec_log.info(f'Recommendations complete\nCall Type: {call_type} Grid: {grid} FDID: {department} Recommendation: {result}\nResponse Plan: {response_plan}\nUnit Ranks: {sorted_unit_log}\nStation Ranks: {station_rank}\nCross Staffing: {cross_staffing_list}\n')
    
    #If no resource requests from the response plan are unfulfilled, return the recommendation
    if not unfulfilled_resources:
        return f"{call_type}: {result}"
    #If there are unfulfilled resource requests, return the recommendation and a list of the unfulfilled resources
    else:
        return f"{call_type}: {result}\nUnfulfilled - {unfulfilled}"
