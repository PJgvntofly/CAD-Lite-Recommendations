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
    connection_log.info("Creating positions\n")
    position = {
        'TAC-1':[],
        'TAC-3':[],
        'TAC-5':[],
        'TAC-7':[]
    }
    for quadrant in station_order.keys():
        if quadrant[:2] == 'BA':
            position['TAC-1'].append(quadrant)
        if quadrant[:2] in ['DF', 'LF', 'BF', 'EF', 'AB', 'TF', 'BE']:
            position['TAC-7'].append(quadrant)
        if quadrant[:2] in ['MF', 'AG', 'AJ', 'BJ', 'SK', 'CA', 'AF', 'AC', 'BH', 'D7', 'NO']:
            position['TAC-5'].append(quadrant)
        if quadrant[:2] in ['AK', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'BI', 'BK', 'DN', 'AW', 'AV', 'AE', 'AD']:
            position['TAC-3'].append(quadrant)
    return position

