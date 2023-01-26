import csv
from log_config import connection_log

def create_station_order():
    station_order = {}
    try:
        f = open(r".\Quadrant Station Order.csv")
        connection_log.info('Importing station orders')
        csv_f = csv.reader(f)
        for row in csv_f:
            quadrant, order = row
            station_order[quadrant] = order.split(",")
        f.close()
        return station_order
    except Exception:
        connection_log.error("")
        print("Error importing station orders")
        return station_order

def create_positions(station_order):
    connection_log.info("Creating positions")
    position = {
        'TAC-1':[],
        'TAC-3':[],
        'TAC-5':[],
        'TAC-2':[]
    }
    connection_log.info("Creating FDIDs\n")
    fdid = {
        '31C02':[],
        '31D01_RFA':[],
        '31D01_CITY':[],
        '31D04':[],
        '31D05':[],
        '31D07':[],
        '31D15':[],
        '31D16':[],
        '31D17':[],
        '31D19':[],
        '31D21':[],
        '31D22':[],
        '31D24':[],
        '31D25':[],
        '31D26':[],
        '31D27':[],
        '31D30':[],
        '31M04':[],
        '31M08':[],
        '31M11':[]
    }
    for quadrant in station_order.keys():
        if quadrant[:2] == 'BA':
            position['TAC-1'].append(quadrant)
            fdid['31M04'].append(quadrant)
        if quadrant[:2] in ['DF', 'LF', 'BF', 'EF', 'AB', 'TF', 'BE']:
            position['TAC-2'].append(quadrant)
        if quadrant[:2] in ['MF', 'AG', 'AJ', 'BJ', 'SK', 'CA', 'AF', 'AC', 'BH', 'D7', 'NO']:
            position['TAC-5'].append(quadrant)
        if quadrant[:2] in ['AK', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'BI', 'BK', 'DN', 'AW', 'AV', 'AE', 'AD']:
            position['TAC-3'].append(quadrant)
        if quadrant[:2] in ['EF', 'BF', 'TF']:
            fdid['31D01_CITY'].append(quadrant)
        if quadrant[:2] in ['DF', 'LF']:
            fdid['31D01_RFA'].append(quadrant)
        if quadrant[:2] == 'AB':
            fdid['31M11'].append(quadrant)
        if quadrant[:2] == 'BE':
            fdid['31C02'].append(quadrant)
        if quadrant[:2] == 'MF':
            fdid['31M08'].append(quadrant)
        if quadrant[:2] == 'AD':
            fdid['31D04'].append(quadrant)
        if quadrant[:2] == 'AE':
            fdid['31D05'].append(quadrant)
        if quadrant[:2] in ['AV', 'AW']:
            fdid['31D26'].append(quadrant)
        if quadrant[:2] == 'AK':
            fdid['31D15'].append(quadrant)
        if quadrant[:2] == 'AL':
            fdid['31D16'].append(quadrant)
        if quadrant[:2] in ['AM', 'AS']:
            fdid['31D17'].append(quadrant)
        if quadrant[:2] == 'AO':
            fdid['31D19'].append(quadrant)
        if quadrant[:2] == 'AQ':
            fdid['31D21'].append(quadrant)
        if quadrant[:2] == 'AR':
            fdid['31D22'].append(quadrant)
        if quadrant[:2] == 'AT':
            fdid['31D24'].append(quadrant)
        if quadrant[:2] == 'AU':
            fdid['31D25'].append(quadrant)
        if quadrant[:2] == 'BI':
            fdid['31D27'].append(quadrant)
        if quadrant[:2] in ['BH', 'AJ', 'BJ']:
            fdid['31D30'].append(quadrant)
        if quadrant[:2] in ['AG', 'AC', 'AF']:
            fdid['31D07'].append(quadrant)
    return position, fdid

if __name__ == '__main__':
    station_order = create_station_order()
    position = create_positions(station_order)
    fdid = position[1]
    position = position[0]
    print(position)