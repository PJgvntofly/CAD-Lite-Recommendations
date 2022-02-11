import recommendations
import units
import station_order

def offline_recommendations(call_type,grid):
    call_type = call_type.strip().upper()
    grid = grid.strip().upper()
    result = []
    skipped_units = []
    list_result = False
    i = 0
    x = 0
    station_rank = {}
    unit_options = []
    unit_rank = {}
    sorted_units = {}
    sorted_unit_list = []
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
    response_plan = radio_position[call_type]
    rec_station_order = station_order.station_order[grid]
    if i <= len(response_plan):
        for unit_type in response_plan:
            list_result = False
            if isinstance(unit_type, list) == True:
                for option in unit_type:
                    if list_result == False:
                        for station in rec_station_order:
                            station_rank[station] = 1 + len(station_rank)
                            for unit in unit_list:
                                if unit.unit_number not in result and unit.unit_number not in skipped_units and unit.unit_type == option and unit.unit_station == station and i < len(response_plan) and unit.unit_status in ['Available', 'AIQ']:
                                    unit_options.append(unit)
                                    for unit in unit_options:
                                        if list_result == False:
                                            unit_rank[unit.unit_number] = station_rank[unit.unit_station]
                                            sorted_units = sorted(unit_rank.items(), key=lambda x: x[1])
                                            for apparatus, station_r in sorted_units:
                                                sorted_unit_list.append(apparatus)
                                                for sorted_unit in sorted_unit_list:
                                                    if sorted_unit not in result and sorted_unit not in skipped_units:
                                                        print(f"\nCall Type: {call_type} | Request: {unit_type} | Recommendation: {sorted_unit}")
                                                        accept = input("Accept recommendation? Enter Y for yes or N to see the next unit. ")
                                                        accept = accept.strip().upper()
                                                        if accept[0] == 'Y':
                                                            result.append(sorted_unit)
                                                            i += 1
                                                            list_result = True
                                                            unit_options = []
                                                            unit_rank = {}
                                                            sorted_units = {}
                                                            sorted_unit_list = []
                                                            continue
                                                        else:
                                                            skipped_units.append(sorted_unit)
                                        else:
                                            continue

                    else:
                        list_result = False
                        continue                               
            else:
                for station in rec_station_order:
                    for unit in unit_list:
                        if unit.unit_type == unit_type and unit.unit_station == station and unit.unit_number not in result and unit.unit_number not in skipped_units and i < len(response_plan) and unit.unit_status in ['Available', 'AIQ']:
                            if list_result == False:
                                print(f"\nCall Type: {call_type} | Request: {unit_type} | Recommendation: {unit.unit_number}")
                                accept = input("Accept recommendation? Enter Y for yes or N to see the next unit. ")
                                accept = accept.strip().upper()
                                if accept[0] == 'Y':
                                    result.append(unit.unit_number)
                                    i += 1
                                    list_result = True
                                    continue
                                else:
                                    skipped_units.append(unit.unit_number)
    else:
        return result
    return f"{call_type}: {result}"

