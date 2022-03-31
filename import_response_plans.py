import json

def import_response_plans():
    response_plans = {}
    with open ('test_response_plans.json') as json_file:
        response_plans = json.load(json_file)
    return response_plans

def update_response_plan(agency_name, zone, response_plan_name, units):
    agency_name = agency_name.upper()
    zone = zone.upper()
    response_plan_name = response_plan_name.upper()
    with open ('test_response_plans.json', 'r+') as json_file:
        data = json.load(json_file)
        if agency_name not in data.keys():
            data.update({agency_name:{zone:{response_plan_name:units}}})
        if agency_name in data.keys() and zone not in data[agency_name].keys():
            data[agency_name].update({zone:{response_plan_name:units}})
        if agency_name in data.keys() and zone in data[agency_name][zone].keys() and response_plan_name not in data[agency_name][zone].keys():
            data[agency_name][zone].update({response_plan_name:units})
        else:
            data[agency_name][zone][response_plan_name] = units
    with open ('test_response_plans.json', 'w') as json_file:
        json.dump(data, json_file)
