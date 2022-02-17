from audioop import cross
import units
import station_order
import logging

TAC_1 = {
    'AIR':['Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'AIRC':['Engine', 'Engine', 'Ladder', 'Medic Unit', 'Engine', 'Medic Unit', 'Aid Unit', 'Aid Unit', 'Tender'],
    'AIRS':['Engine'],
    'BLS':[['Aid Unit', 'Engine', 'Ladder']],
    'BLSN':[['Aid Unit', 'Engine', 'Ladder']],
    'COA':['Engine'],
    'COAM':['Engine', 'Medic Unit', 'Command Unit'],
    'FAC':[['Engine', 'Ladder']],
    'FS':[['Engine', 'Ladder']],
    'FTU':[['Engine', 'Ladder']],
    'FFB':['Ladder', 'Engine', 'Engine', 'Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'FAR':[['Engine', 'Ladder']],
    'FAS':[['Engine', 'Ladder']],
    'FB':['Engine'],
    'FCC':['Engine', 'Engine', 'Ladder', 'Engine', 'Engine', 'Medic Unit', ['Aid Unit', 'Medic Unit'], 'Ladder', 'Command Unit', 'Medical Services Officer'],
    'FI':[],
    'FRC':['Engine', 'Engine', 'Ladder', 'Engine', 'Engine', 'Medic Unit', ['Aid Unit', 'Medic Unit'], 'Command Unit', 'Medical Services Officer'],
    'FSN':[['Engine', 'Ladder']],
    'GLI':['Engine', ['Engine', 'Ladder'], 'Command Unit'],
    'GLO':[['Engine', 'Ladder'], 'Engine'],
    'HZ':[['Engine', 'Ladder'], 'Engine', 'Command Unit'],
    'HZ2':['HazMat', 'Decon', 'Engine', 'Medic Unit'],
    'HZ3':['Engine', 'HazMat', 'HazMat', 'Air Unit'],
    'MCI':[['Engine', 'Ladder'], 'Medic Unit', 'Engine', 'Medic Unit', 'Aid Unit', 'Aid Unit', 'Engine', 'Aid Unit', 'Aid Unit', 'Command Unit', 'Command Unit'],
    'MED':['Medic Unit', 'Engine'],
    'MEDX':['Medic Unit', ['Engine', 'Ladder'], ['Engine', 'Ladder'], 'Medical Services Officer'],
    'MVC':[['Engine', 'Ladder']],
    'MVCE':['Engine', 'Ladder', 'Medic Unit', 'Command Unit', 'Medical Services Officer'],
    'MVCF':[['Engine', 'Ladder'], 'Engine', 'Medic Unit', 'Command Unit', 'Medical Services Officer'],
    'MVCM':[['Engine', 'Ladder'], 'Medic Unit'],
    'MVCN':[['Engine', 'Ladder']],
    'MVCP':[['Engine', 'Ladder'], 'Medic Unit'],
    'RESA':[['Engine','Ladder'], ['Medic Unit', 'Aid Unit'], 'Engine', 'Command Unit'],
    'RESA2':['Technical Rescue', 'Ladder', 'Engine', 'Medic Unit', 'Command Unit'],
    'RESA3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder'], 'Medic Unit'],
    'RESA4':['Engine', 'Command Unit'],
    'RESCS':[],
    'RESCS2':['Technical Rescue', 'Ladder', 'HazMat', 'Engine', 'Medic Unit', 'Aid Unit', 'Air Unit'],
    'RESCS3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder'], 'Command Unit'],
    'RESST':['Engine', ['Engine', 'Ladder'], 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'RESST2':['Technical Rescue', 'Engine', 'Ladder', 'Command Unit'],
    'RESST3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder'], ['Medic Unit', 'Aid Unit']],
    'RESSW':['Fire Boat', ['Engine', 'Ladder'], 'Medic Unit', 'Command Unit'],
    'RESTR':[],
    'RESTR2':['Technical Rescue', 'Ladder', 'HazMat', 'Engine', 'Medic Unit', 'Air Unit', 'Command Unit'],
    'RESTR3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder']],
    'RESWA':['Fire Boat', ['Engine', 'Ladder'], 'Medic Unit', 'Command Unit'],
    'SC':[['Engine', 'Ladder']]
}

TAC_7 = {
    'AIR':['Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'AIRC':['Engine', 'Engine', 'Ladder', 'Medic Unit', 'Engine', 'Medic Unit', 'Aid Unit', 'Aid Unit', 'Tender'],
    'AIRS':['Engine'],
    'BLS':[['Aid Unit', 'Medic Unit', 'Engine', 'Ladder']],
    'BLSN':[['Aid Unit', 'Medic Unit', 'Engine', 'Ladder']],
    'COA':[['Engine', 'Ladder']],
    'COAM':['Engine', 'Medic Unit', 'Command Unit'],
    'FAC':[['Engine', 'Ladder']],
    'FS':[['Engine', 'Ladder']],
    'FTU':[['Engine', 'Ladder']],
    'FFB':['Ladder', 'Engine', 'Engine', 'Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'FAR':[['Engine', 'Ladder']],
    'FAS':[['Engine', 'Ladder']],
    'FB':[['Engine', 'Ladder']],
    'FCC':['Ladder', 'Engine', 'Engine', 'Engine', 'Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'FI':[],
    'FRC':['Ladder', 'Engine', 'Engine', 'Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'FSN':[['Engine' , 'Ladder']],
    'GLI':['Engine', ['Engine', 'Ladder'], 'Command Unit'],
    'GLO':[['Engine', 'Ladder'], 'Engine'],
    'HZ':[['Engine', 'Ladder']],
    'HZ2':['HazMat','Decon','Engine','Medic Unit'],
    'HZ3':['Engine', 'HazMat', 'HazMat', 'Air Unit'],
    'MCI':[['Engine', 'Ladder'], 'Medic Unit', 'Engine', 'Medic Unit', 'Aid Unit', 'Aid Unit', 'Engine', 'Aid Unit', 'Aid Unit', 'Command Unit', 'Command Unit'],
    'MED':['Medic Unit', ['Engine', 'Aid Unit', 'Ladder']],
    'MEDX':['Medic Unit', ['Engine', 'Ladder'], 'Medic Unit', 'Command Unit'],
    'MVC':[['Engine', 'Ladder'], ['Aid Unit', 'Medic Unit']],
    'MVCE':[['Engine', 'Ladder'], 'Medic Unit', 'Aid Unit', 'Engine', 'Command Unit'],
    'MVCF':[['Engine', 'Ladder'], 'Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'MVCM':[['Engine', 'Ladder'], 'Medic Unit', 'Aid Unit', 'Engine', 'Command Unit'],
    'MVCN':[['Engine', 'Ladder'], 'Aid Unit'],
    'MVCP':[['Engine', 'Ladder'], 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'RESA':[['Engine', 'Ladder'], ['Medic Unit', 'Aid Unit'], 'Engine', 'Command Unit'],
    'RESA2':['Technical Rescue', 'Ladder', 'Engine', 'Medic Unit', 'Command Unit'],
    'RESA3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder'], 'Medic Unit'],
    'RESA4':['Engine', 'Command Unit'],
    'RESCS':[],
    'RESCS2':['Technical Rescue', 'Ladder', 'Engine', 'HazMat', 'Engine', 'Medic Unit', 'Aid Unit'],
    'RESCS3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder'], 'Command Unit'],
    'RESST':['Engine', ['Engine', 'Ladder'], 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'RESST2':['Technical Rescue', 'Engine', 'Ladder', 'Command Unit'],
    'RESST3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder'], ['Medic Unit', 'Aid Unit']],
    'RESSW':['Fire Boat', ['Engine', 'Ladder'], 'Medic Unit', 'Command Unit'],
    'RESTR':[],
    'RESTR2':['Technical Rescue', 'Ladder', 'HazMat', 'Engine', 'Medic Unit', 'Air Unit', 'Command Unit'],
    'RESTR3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder']],
    'RESWA':['Fire Boat', ['Engine', 'Ladder'], 'Medic Unit', 'Command Unit'],
    'SC':[['Engine', 'Ladder']]
    }

TAC_5 = {
    'AIR':['Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'AIRC':['Engine', 'Engine', 'Ladder', 'Medic Unit', 'Engine', 'Medic Unit', 'Aid Unit', 'Aid Unit', 'Tender'],
    'AIRS':['Engine'],
    'BLS':['Aid Unit'],
    'BLSN':['Aid Unit'],
    'COA':['Engine', 'Command Unit'],
    'COAM':['Engine', 'Medic Unit', 'Command Unit'],
    'FAC':['Engine'],
    'FS':['Engine'],
    'FTU':['Engine'],
    'FFB':['Ladder', 'Engine', 'Engine', 'Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'FAR':['Engine'],
    'FAS':['Engine'],
    'FB':['Brush Truck', 'Brush Truck', 'Engine', 'Tender'],
    'FCC':['Engine', 'Engine', 'Ladder', 'Engine', 'Medic Unit', 'Command Unit'],
    'FCC - No Hydrant':['Engine', 'Engine', 'Ladder', 'Engine', 'Tender', 'Medic Unit' , 'Command Unit'],
    'FI':[],
    'FRC':['Engine', ['Engine', 'Ladder'], 'Ladder', 'Medic Unit', 'Engine', 'Command Unit'],
    'FRC - No Hydrant':['Engine', ['Engine', 'Ladder'], 'Tender', 'Engine', 'Medic Unit', 'Tender', 'Command Unit'],
    'FSN':[['Engine', 'Ladder']],
    'GLI':['Engine', ['Engine', 'Ladder'], 'Command Unit'],
    'GLO':[['Engine', 'Ladder'], 'Engine'],
    'HZ':[['Engine', 'Ladder'], 'Engine', 'Command Unit'],
    'HZ2':['HazMat', 'Decon', 'Engine', 'Medic Unit'],
    'HZ3':['Engine', 'HazMat', 'HazMat', 'Air Unit'],
    'MCI':[['Engine', 'Ladder'], 'Medic Unit', 'Engine', 'Medic Unit', 'Aid Unit', 'Aid Unit', 'Aid Unit', 'Engine', 'Aid Unit', 'Aid Unit', 'Command Unit', 'Command Unit'],
    'MED':['Medic Unit', ['Engine', 'Aid Unit']],
    'MEDX':['Medic Unit', ['Engine', 'Ladder'], 'Medic Unit', 'Command Unit'],
    'MVC':[['Engine', 'Ladder'], 'Aid Unit', 'Command Unit'],
    'MVCE':[['Engine', 'Ladder'], 'Medic Unit', 'Aid Unit', 'Engine', 'Command Unit'],
    'MVCF':[['Engine', 'Ladder'], 'Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'MVCM':[['Engine', 'Ladder'], 'Medic Unit', 'Aid Unit', 'Engine', 'Command Unit'],
    'MVCN':[['Engine', 'Ladder'], 'Aid Unit'],
    'MVCP':['Medic Unit', ['Engine', 'Ladder'], 'Command Unit'],
    'RESA':[['Engine', 'Ladder'], ['Medic Unit', 'Aid Unit'], 'Engine', 'Command Unit'],
    'RESA2':['Technical Rescue', 'Ladder', 'Engine', 'Medic Unit', 'Command Unit'],
    'RESA3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder'], 'Medic Unit'],
    'RESA4':['Engine', 'Command Unit'],
    'RESCS':[],
    'RESCS2':['Technical Rescue', 'Ladder', 'HazMat', 'Engine', 'Medic Unit', 'Aid Unit', 'Air Unit'],
    'RESCS3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder'], 'Command Unit'],
    'RESST':['Engine', ['Engine', 'Ladder'], 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'RESST2':['Technical Rescue', 'Engine', 'Ladder', 'Command Unit'],
    'RESST3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder'], ['Medic Unit', 'Aid Unit']],
    'RESSW':['Fire Boat', ['Engine', 'Ladder'], 'Medic Unit', 'Command Unit'],
    'RESTR':[],
    'RESTR2':['Technical Rescue', 'Ladder', 'HazMat', 'Engine', 'Medic Unit', 'Air Unit', 'Command Unit'],
    'RESTR3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder']],
    'RESWA':['Fire Boat', ['Engine', 'Ladder'], 'Medic Unit', 'Command Unit'],
    'SC':[['Engine', 'Ladder']]
}

TAC_3 = {
    'AIR':['Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'AIRC':['Engine', 'Engine', 'Ladder', 'Medic Unit', 'Engine', 'Medic Unit', 'Aid Unit', 'Aid Unit', 'Tender'],
    'AIRS':['Engine'],
    'BLS':[['Aid Unit', 'Medic Unit', 'Engine', 'Ladder']],
    'BLSN':[['Aid Unit', 'Medic Unit', 'Engine', 'Ladder']],
    'COA':[['Engine', 'Ladder']],
    'COAM':['Engine', 'Medic Unit', 'Command Unit'],
    'FAC':[['Engine', 'Ladder']],
    'FS':[['Engine', 'Ladder']],
    'FTU':[['Engine', 'Ladder']],
    'FFB':['Ladder', 'Engine', 'Engine', 'Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'FAR':[['Engine', 'Ladder']],
    'FAS':[['Engine', 'Ladder']],
    'FB':[['Engine', 'Ladder']],
    'FCC':['Ladder', 'Engine', 'Engine', 'Engine', 'Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'FCC - No Hydrant':['Engine', 'Engine', 'Ladder', 'Engine', 'Tender', 'Medic Unit' , 'Command Unit'],
    'FI':[],
    'FRC':['Ladder' 'Engine', 'Engine', 'Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'FRC - No Hydrant':['Engine', ['Engine', 'Ladder'], 'Tender', 'Engine', 'Medic Unit', 'Tender', 'Command Unit'],
    'FSN':[['Engine' , 'Ladder']],
    'GLI':['Engine', ['Engine', 'Ladder'], 'Command Unit'],
    'GLO':[['Engine', 'Ladder'], 'Engine'],
    'HZ':[['Engine', 'Ladder']],
    'HZ2':['HazMat','Decon','Engine','Medic Unit'],
    'HZ3':['Engine', 'HazMat', 'HazMat', 'Air Unit'],
    'MCI':[['Engine', 'Ladder'], 'Medic Unit', 'Engine', 'Medic Unit', 'Aid Unit', 'Aid Unit', 'Engine', 'Aid Unit', 'Aid Unit', 'Command Unit', 'Command Unit'],
    'MED':['Medic Unit', ['Engine', 'Aid Unit', 'Ladder']],
    'MEDX':['Medic Unit', ['Engine', 'Ladder'], 'Medic Unit', 'Command Unit'],
    'MVC':[['Engine', 'Ladder'], ['Aid Unit', 'Medic Unit']],
    'MVCE':[['Engine', 'Ladder'], 'Medic Unit', 'Aid Unit', 'Engine', 'Command Unit'],
    'MVCF':[['Engine', 'Ladder'], 'Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'MVCM':[['Engine', 'Ladder'], 'Medic Unit', 'Aid Unit', 'Engine', 'Command Unit'],
    'MVCN':[['Engine', 'Ladder'], 'Aid Unit'],
    'MVCP':['Medic Unit', ['Engine', 'Ladder'], 'Command Unit'],
    'RESA':[['Engine', 'Ladder'], ['Medic Unit', 'Aid Unit'], 'Engine', 'Command Unit'],
    'RESA2':['Technical Rescue', 'Ladder', 'Engine', 'Medic Unit', 'Command Unit'],
    'RESA3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder'], 'Medic Unit'],
    'RESA4':['Engine', 'Command Unit'],
    'RESCS':[],
    'RESCS2':['Technical Rescue', 'Ladder', 'HazMat', 'Engine', 'Medic Unit', 'Aid Unit', 'Air Unit'],
    'RESCS3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder'], 'Command Unit'],
    'RESST':['Engine', ['Engine', 'Ladder'], 'Medic Unit', 'Aid Unit', 'Command Unit'],
    'RESST2':['Technical Rescue', 'Engine', 'Ladder', 'Command Unit'],
    'RESST3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder'], ['Medic Unit', 'Aid Unit']],
    'RESSW':['Fire Boat', ['Engine', 'Ladder'], 'Medic Unit', 'Command Unit'],
    'RESTR':[],
    'RESTR2':['Technical Rescue', 'Ladder', 'HazMat', 'Engine', 'Medic Unit', 'Air Unit', 'Command Unit'],
    'RESTR3':['Technical Rescue', 'Technical Rescue', 'Technical Rescue', ['Engine', 'Ladder']],
    'RESWA':['Fire Boat', ['Engine', 'Ladder'], 'Medic Unit', 'Command Unit'],
    'SC':[['Engine', 'Ladder']]
    }
station_orders = station_order.create_station_order()
position = station_order.create_positions(station_orders)

def get_radio(val):
    for key, values in position.items():
        if val in values:
            return key

def find_hydrant(call, radio_position):
    if radio_position in [TAC_3, TAC_5] and call in ['FCC', 'FRC']:
        no_hydrant = ""
        no_hydrant = input('Is this call in a No Hydrant area? Enter Y for yes and N for no:')
        no_hydrant = no_hydrant.strip().upper()
        no_hydrant = no_hydrant[0]
        if no_hydrant == "Y":
            return call + " - No Hydrant"
        if no_hydrant not in ['Y', 'N']:
            print('Please enter only Y or N \nIf call is in a No Hydrant area, please enter the information again.')
    return call

def recommendations(call_type,grid):
    logging.info("Beginning recommendations")
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
    unit_list = units.refresh_units()
    if radio_position == 'TAC_1':
        radio_position = TAC_1
    if radio_position == 'TAC_7':
        radio_position = TAC_7
    if radio_position == 'TAC_5':
        radio_position = TAC_5
    if radio_position == 'TAC_3':
        radio_position = TAC_3
    elif radio_position == None:
        return print("Quadrant not supported")
    call_type = find_hydrant(call_type, radio_position)
    response_plan = radio_position[call_type]
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
                        if unit.unit_type == unit_type and unit.unit_station == station and unit.unit_number not in result and unit.unit_number not in cross_staffing_list and i < len(response_plan) and unit.unit_status in ['Available', 'AIQ']:
                            if list_result == False:
                                result.append(unit.unit_number)
                                if unit.cross_staffing is not None:
                                    cross_staffing_list.extend(unit.cross_staffing)
                                i += 1
                                list_result = True
    else:
        return result
    logging.info(f'Recommendations complete\nCall Type: {call_type} Grid: {grid} Recommendation: {result}\nResponse Plan: {response_plan}\nUnit Ranks: {sorted_unit_log}\nStation Ranks: {station_rank}\nCross Staffing: {cross_staffing_list}\n')
    return f"{call_type}: {result}"
