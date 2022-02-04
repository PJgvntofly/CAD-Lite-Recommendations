import units
import station_order

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
    'FRC':['Ladder' 'Engine', 'Engine', 'Engine', 'Medic Unit', 'Aid Unit', 'Command Unit'],
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

position = station_order.create_positions()

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
    if call_type in ['RESCS', 'RESTR']:
        return print("Use second alarm type code: {}".format(call_type + "2"))
    radio_position = get_radio(grid)
    units.refresh_units()
    if radio_position == 'TAC_1':
        radio_position = TAC_1
    if radio_position == 'TAC_7':
        radio_position = TAC_7
    if radio_position == 'TAC_5':
        radio_position = TAC_5
    if radio_position == 'TAC_3':
        radio_position = TAC_3
    call_type = find_hydrant(call_type, radio_position)
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
                            for unit in units.unit_list:
                                if unit.unit_number not in result and unit.unit_type == option and unit.unit_station == station and i < len(response_plan) and unit.unit_status in ['Available', 'AIQ']:
                                    unit_options.append(unit)
                                    for unit in unit_options:
                                        if list_result == False:
                                            unit_rank[unit.unit_number] = station_rank[unit.unit_station]
                                            sorted_units = sorted(unit_rank.items(), key=lambda x: x[1])
                                            for apparatus, station_r in sorted_units:
                                                sorted_unit_list.append(apparatus)
                                                result.append(sorted_unit_list[0])
                                                i += 1
                                                list_result = True
                                                unit_options = []
                                                unit_rank = {}
                                                sorted_units = {}
                                                sorted_unit_list = []
                    else:
                        list_result = False
                        continue                               
            else:
                for station in rec_station_order:
                    for unit in units.unit_list:
                        if unit.unit_type == unit_type and unit.unit_station == station and unit.unit_number not in result and i < len(response_plan) and unit.unit_status in ['Available', 'AIQ']:
                            if list_result == False:
                                result.append(unit.unit_number)
                                i += 1
                                list_result = True
    else:
        return result
    return f"{call_type}: {result}"
