import json

def import_response_plans():
    response_plans = {}
    with open ('test_response_plans.json') as json_file:
        response_plans = json.load(json_file)
    return response_plans

def update_response_plan(agency_name, response_plan_name, units):
    #agency_name = input("Please enter the agency name: ")
    #response_plan_name = input("Please enter the response plan name: ")
    #units = (input('Please enter the unit request(s) seperated by a comma: '))
    agency_name = agency_name.upper()
    response_plan_name = response_plan_name.upper()
    with open ('test_response_plans.json', 'r+') as json_file:
        data = json.load(json_file)
        if agency_name not in data.keys():
            data.update({agency_name:{response_plan_name:[units]}})
        elif agency_name in data.keys() and response_plan_name not in data[agency_name].keys():
            data[agency_name].update({response_plan_name:[units]})
        else:
            if isinstance(units, list):
                data[agency_name][response_plan_name] = units
            else:
                data[agency_name][response_plan_name] = list(units)
    with open ('test_response_plans.json', 'w') as json_file:
        json.dump(data, json_file)
