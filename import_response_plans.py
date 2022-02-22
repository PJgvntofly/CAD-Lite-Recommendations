import json

def import_response_plans():
    response_plans = {}
    with open ('response_plans.json') as json_file:
        response_plans = json.load(json_file)
    return response_plans

if __name__ == "__main__":
    import_response_plans()