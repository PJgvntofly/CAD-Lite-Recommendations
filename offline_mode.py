from import_response_plans import import_response_plans
import recommendations
import units
from datetime import datetime
from log_config import rec_log
import PySimpleGUI as sg

frls = import_response_plans()

def offline_recommendations(call_type,grid):
    rec_log.info("Beginning offline recommendations")
    call_type = call_type.strip().upper()
    grid = grid.strip().upper()
    result = []
    skipped_units = []
    list_result = False
    i = 0
    station_rank = {}
    unit_options = []
    unit_rank = {}
    sorted_units = {}
    sorted_unit_list = []
    cross_staffing_list = []
    cross_staff_dict = {}
    options = []
    sorted_unit_log = {}
    station_rank_log = {}
    if call_type in ['RESCS', 'RESTR']:
        return print("Use second alarm type code: {}".format(call_type + "2"))
    radio_position = recommendations.get_radio(grid)
    unit_list = units.import_units()
    if radio_position == 'TAC_1':
        radio_position = recommendations.TAC_1
    if radio_position == 'TAC_7':
        radio_position = recommendations.TAC_7
    if radio_position == 'TAC_5':
        radio_position = recommendations.TAC_5
    if radio_position == 'TAC_3':
        radio_position = recommendations.TAC_3
    call_type = recommendations.find_hydrant(call_type, radio_position)
    agency = 'SNO911'
    if grid in frls[agency].keys() and call_type in frls[agency][grid].keys():
        response_plan = frls[agency][grid][call_type]
    else:
        response_plan = frls[agency][radio_position][call_type]
    rec_station_order = recommendations.station_orders[grid]
    if i <= len(response_plan):
        for unit_type in response_plan:
            list_result = False
            if isinstance(unit_type, list):
                for option in unit_type:
                    options.append(option)
                for station in rec_station_order:
                    station_rank[station] = 1 + len(station_rank)
                    for unit in unit_list:
                        if unit.unit_number not in result and unit.unit_number not in skipped_units and unit.unit_number not in cross_staffing_list and unit.unit_type in options and unit.unit_station == station and i < len(response_plan) and unit.unit_status in ['Available', 'AIQ']:
                            unit_options.append(unit)
                for unit in unit_options:
                    if list_result == False:
                        unit_rank[unit.unit_number] = station_rank[unit.unit_station]
                        cross_staff_dict[unit.unit_number] = unit.cross_staffing
                    else:
                        continue
                sorted_units = sorted(unit_rank.items(), key=lambda x: x[1])
                for apparatus, station_r in sorted_units:
                    sorted_unit_list.append(apparatus)
                for sorted_unit in sorted_unit_list:
                    if list_result == False:
                        if sorted_unit not in result and sorted_unit not in skipped_units:
                            accept = sg.popup_get_text(f"Call Type: {call_type} | Request: {unit_type} | Recommendation: {sorted_unit}\nAccept recommendation? Enter Y for yes or N to see the next unit. ",title='Offline Mode')
                            try:
                                accept = accept.strip().upper()
                                if accept[0] == 'Y':
                                    result.append(sorted_unit)
                                    cross_staffing_list.extend(cross_staff_dict[sorted_unit])
                                    sorted_unit_log[sorted_unit] = sorted_units
                                    station_rank_log[sorted_unit] = station_rank
                                    i += 1
                                    list_result = True
                                    unit_options = []
                                    unit_rank = {}
                                    sorted_units = {}
                                    sorted_unit_list = []
                                    continue
                                else:
                                    skipped_units.append(sorted_unit)
                                    cross_staffing_list.extend(cross_staff_dict[sorted_unit])
                            except AttributeError as err:
                                rec_log.error(err)
                                break
                    else:   
                        continue                              
            else:
                for station in rec_station_order:
                    for unit in unit_list:
                        if unit.unit_type == unit_type and unit.unit_station == station and unit.unit_number not in result and unit.unit_number not in skipped_units  and unit.unit_number not in cross_staffing_list and i < len(response_plan) and unit.unit_status in ['Available', 'AIQ']:
                            if list_result == False:
                                accept = sg.popup_get_text(f"Call Type: {call_type} | Request: {unit_type} | Recommendation: {unit.unit_number}\nAccept recommended unit? Enter Y for yes or N to see the next unit. ",title='Offline Mode')
                                try:
                                    accept = accept.strip().upper()
                                    if accept[0] == 'Y':
                                        result.append(unit.unit_number)
                                        cross_staffing_list.extend(unit.cross_staffing)
                                        i += 1
                                        list_result = True
                                        continue
                                    else:
                                        skipped_units.append(unit.unit_number)
                                except AttributeError as err:
                                    rec_log.exception(err)
                                    break
    else:
        return result
    rec_log.info(f'OFFLINE MODE\nTime: {str(datetime.now())}\nCall Type: {call_type} Grid: {grid} Recommendation: {result}\nResponse Plan: {response_plan}\n Skipped Units: {skipped_units}\nUnit Ranks: {sorted_unit_log}\nStation Ranks: {station_rank}\nCross Staffing: {cross_staffing_list}\n')
    return f"\nRecommendation:\n{call_type}: {result}"

