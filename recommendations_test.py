from offline_mode import offline_recommendations
import recommendations
import station_order
import re
import os

def test_recommendations():
    pattern = '\[([A-Z0-9, ]+)\]'
    errors = []
    error = ""
    for call_type in recommendations.TAC_1.keys():
        for quadrant in station_order.station_order.keys():
            result = recommendations.recommendations(call_type, quadrant)
            radio_position = recommendations.get_radio(quadrant)
            if radio_position == 'TAC_1':
                radio_position = recommendations.TAC_1
            if radio_position == 'TAC_7':
                radio_position = recommendations.TAC_7
            if radio_position == 'TAC_5':
                radio_position = recommendations.TAC_5
            if radio_position == 'TAC_3':
                radio_position = recommendations.TAC_3
            matches = re.match(pattern, str(result))
            if matches != None:
                if len(matches[1].split(", ")) != len(radio_position[call_type]):
                    error = f"{call_type} {quadrant} Result:{result}"
                    errors.append(error)
    return errors

def create_log(returned_errors):
    with open(os.path.expanduser('~') + '\errors_found.txt', 'w') as file:
        for error in returned_errors:
            file.write(error)
    file.close

if __name__ == "__main__":
    returned_errors = test_recommendations()
    create_log(returned_errors)
