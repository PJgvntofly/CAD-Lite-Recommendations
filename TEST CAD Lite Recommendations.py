from typing import List


position = {
    'TAC_1':['BA0001', 'BA0002', 'BA0003', 'BA0004'],
    'TAC_7':['DF009', 'DF010', 'DF011', 'DF013', 'DF055']
}

TAC_1 = {
    'BLS':[['Aid Unit', 'Engine', 'Ladder']],
    'BLSN':[['Aid Unit', 'Engine', 'Ladder']],
    'MED':['Medic Unit', 'Engine'],
    'MEDX':['Medic Unit', ['Engine', 'Ladder'], ['Engine', 'Ladder'], 'Medical Services Officer'],
    'HZ':[['Engine','Ladder'], 'Engine', 'Command Unit']
}

station_order = {
    'BA0001':['STA 2', 'STA 3', 'STA 1', 'STA 5', 'STA 4', 'STA 6', 'STA 7', 'STA 61', 'STA 63', 'STA 82'],
    'BA0002':['STA 2', 'STA 3', 'STA 1', 'STA 5', 'STA 4', 'STA 6', 'STA 7', 'STA 61', 'STA 63', 'STA 82']
}

class Unit:
    def __init__(self, unit_number, unit_type, unit_station):
        self.unit_number = unit_number
        self.unit_type = unit_type
        self.unit_station = unit_station
    def __str__(self):
        return f"{self.unit_number}"

A2 = Unit("A2", "Aid Unit", "STA 2")
E2 = Unit("E2","Engine","STA 2")
E15 = Unit("E15","Engine","STA 15")
M1 = Unit("M1", "Medic Unit","STA 1")
MSO5 = Unit("MSO5", "Medical Services Officer", "STA 5")
L1 = Unit("L1","Ladder","STA 1")
L1A = Unit("L1A","Ladder","STA 1")
E1 = Unit("E1","Engine","STA 1")
B1 = Unit("B1","Command Unit", "STA 5")

class Unit_List:
    def __init__(self):
        self.list = {}
    def add_unit(self,Unit):
        self.list[Unit] = Unit
    def __str__(self):
        return f"{self.list()}"

fire_list = Unit_List()
fire_list.add_unit(A2)
fire_list.add_unit(E2)
fire_list.add_unit(E15)
fire_list.add_unit(M1)
fire_list.add_unit(MSO5)
fire_list.add_unit(L1)
fire_list.add_unit(L1A)
fire_list.add_unit(E1)
fire_list.add_unit(B1)

def get_radio(val):
    for key, values in position.items():
        if val in values:
            return key

def recommendations(call_type,grid):
    call_type = call_type.strip().upper()
    grid = grid.strip().upper()
    result = []
    list_result = False
    i = 0
    radio_position = get_radio(grid)
    if radio_position == 'TAC_1':
        radio_position = TAC_1
    response_plan = radio_position[call_type]
    rec_station_order = station_order[grid]
    if i <= len(response_plan):
        for unit_type in response_plan:
            if isinstance(unit_type, list) == True:
                for option in unit_type:
                    if list_result == False:
                        for station in rec_station_order:
                            for unit in fire_list.list:
                                if unit.unit_type == option and unit.unit_station == station and unit.unit_number not in result and i < len(response_plan):
                                    result.append(unit.unit_number)
                                    i += 1
                                    list_result = True
                    else:
                        list_result = False
                        continue                               
            else:
                for station in rec_station_order:
                    for unit in fire_list.list:
                        if unit.unit_type == unit_type and unit.unit_station == station and unit.unit_number not in result and i < len(response_plan):
                            result.append(unit.unit_number)
                            i += 1
                            list_result = True
    else:
        return result
    return f"{call_type}: {result}"

print(recommendations('bls','BA0002'))
print(recommendations('medx','BA0001'))
print(recommendations('Hz', 'BA0001'))


