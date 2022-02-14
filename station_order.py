import csv

station_order = {}
f = open(r"P:\DISPATCH\Manual Operations\CAD Lite Recommendations\Quadrant Station Order.csv")
csv_f = csv.reader(f)
for row in csv_f:
    quadrant, order = row
    station_order[quadrant] = order.split(",")
f.close()

def create_positions():
    position = {
        'TAC_1':[],
        'TAC_3':[],
        'TAC_5':[],
        'TAC_7':[]
    }
    for quadrant in station_order.keys():
        if quadrant[:2] == 'BA':
            position['TAC_1'].append(quadrant)
        if quadrant[:2] in ['DF', 'LF', 'BF', 'EF', 'AB', 'TF', 'BE']:
            position['TAC_7'].append(quadrant)
        if quadrant[:2] in ['MF', 'AG', 'AJ', 'BJ', 'SK', 'CA', 'AF', 'AC', 'BH', 'D7', 'NO']:
            position['TAC_5'].append(quadrant)
        if quadrant[:2] in ['AK', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'BI', 'BK', 'DN', 'AW']:
            position['TAC_3'].append(quadrant)
    return position

