import PySimpleGUI as sg
import units
import station_order
from log_config import rec_log, connection_log
from import_response_plans import import_response_plans

station_orders = station_order.create_station_order()
position = station_order.create_positions(station_orders)
frls = import_response_plans()

def get_radio(val):
    for key, values in position.items():
        if val in values:
            return key

def find_hydrant(call, radio_position):
    if radio_position in ['TAC-3', 'TAC-5'] and call in ['FCC', 'FRC']:
        no_hydrant_response = False
        no_hydrant = ""
        while no_hydrant_response is False:
            no_hydrant = sg.popup_get_text('Is this call in a No Hydrant area? Enter Y for yes and N for no:',title='No Hydrant Area')
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
                continue
    return call

def recommendations(call_type,grid):
    rec_log.info("Beginning recommendations")
    call_type = call_type.strip().upper()
    grid = grid.strip().upper()
    result = []
    list_result = False
    i = 0
    station_rank = {}
    unit_options = []
    unit_rank = {}
    sorted_units = {}
    sorted_unit_list = []
    unit_list = []
    cross_staffing_list = []
    cross_staff_dict = {}
    options = []
    sorted_unit_log = {}
    station_rank_log = {}
    if call_type in ['RESCS', 'RESTR']:
        return print("Use second alarm type code: {}".format(call_type + "2"))
    radio_position = get_radio(grid)
    connection_log.info('Initializing database connection')
    unit_list = units.refresh_units()
    if radio_position == None:
        return print("Quadrant not supported")
    call_type = find_hydrant(call_type, radio_position)
    if grid in station_orders:
        agency = 'SNO911'
    if grid in frls[agency].keys() and call_type in frls[agency][grid].keys():
        response_plan = frls[agency][grid][call_type]
    else:
        response_plan = frls[agency][radio_position][call_type]
    rec_station_order = station_orders[grid]
    for station in rec_station_order:
        station_rank[station] = 1 + len(station_rank)
    if i <= len(response_plan):
        for unit_type in response_plan:
            list_result = False
            if isinstance(unit_type, list) == True:
                for option in unit_type:
                    options.append(option)
                for unit in unit_list:
                    rec_log.debug(f'Unit: {unit.unit_number} Status: {unit.unit_status} Type: {unit.unit_type} Station: {unit.unit_station}')
                    if unit.unit_number not in result and unit.unit_number not in cross_staffing_list and unit.unit_type in options and unit.unit_station in rec_station_order and i < len(response_plan) and unit.unit_status in ['Available', 'AIQ']:
                        unit_options.append(unit)
                for unit in unit_options:
                    if list_result == False:
                        unit_rank[unit.unit_number] = station_rank[unit.unit_station]
                        if unit.cross_staffing is not None:
                            cross_staff_dict[unit.unit_number] = unit.cross_staffing
                    else:
                        continue
                sorted_units = sorted(unit_rank.items(), key=lambda x: x[1])
                for apparatus, station_r in sorted_units:
                    sorted_unit_list.append(apparatus)
                for sorted_unit in sorted_unit_list:
                    if list_result == False: 
                        result.append(sorted_unit)
                        if sorted_unit in cross_staff_dict.keys():
                            cross_staffing_list.extend(cross_staff_dict[sorted_unit])
                        sorted_unit_log[sorted_unit] = sorted_units
                        station_rank_log[sorted_unit] = station_rank
                        i += 1
                        list_result = True
                        options = []
                        unit_options = []
                        unit_rank = {}
                        sorted_units = {}
                        sorted_unit_list = []
                        continue
                    else:
                        continue                               
            else:
                for station in rec_station_order:
                    for unit in unit_list:
                        rec_log.debug(f'Unit: {unit.unit_number} Status: {unit.unit_status} Type: {unit.unit_type} Station: {unit.unit_station}')
                        if unit.unit_type == unit_type and unit.unit_station == station and unit.unit_number not in result and unit.unit_number not in cross_staffing_list and i < len(response_plan) and unit.unit_status in ['Available', 'AIQ']:
                            if list_result == False:
                                result.append(unit.unit_number)
                                if unit.cross_staffing is not None:
                                    cross_staffing_list.extend(unit.cross_staffing)
                                i += 1
                                list_result = True
    else:
        return result
    rec_log.info(f'Recommendations complete\nCall Type: {call_type} Grid: {grid} Recommendation: {result}\nResponse Plan: {response_plan}\nUnit Ranks: {sorted_unit_log}\nStation Ranks: {station_rank}\nCross Staffing: {cross_staffing_list}\n')
    return f"{call_type}: {result}"
