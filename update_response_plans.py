from urllib import response
import json

def create_new_agency():
    new_agency_name = input("Please enter the agency name: ")
    response_plan_name = input("Please enter a response plan name: ")
    response = []
    keep_going = True
    while keep_going is True:
        try:
            print('Hit ctrl + c when finished')
            response.append(input('Please enter the unit request: '))
        except KeyboardInterrupt:
            keep_going = False
    with open ('response_plans.json', 'r+') as json_file:
        data = json.load(json_file)
        data.update({new_agency_name:{response_plan_name:[response]}})
    json.dump(data, open('test_response_plans.json', 'w'))

create_new_agency()
