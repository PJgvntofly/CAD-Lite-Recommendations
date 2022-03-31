#Create GUI for CAD Lite Recommendations

from urllib import response
import PySimpleGUI as sg
from get_recommendations import get_recommendations
from import_response_plans import import_response_plans

entry_mask = [
    [
        sg.Text("Call Type"),
        sg.In(size=(15,1), key="-CALL TYPE-")
    ],
    [
        sg.Text("Grid       "),
        sg.In(size=(15,1), key="-GRID-")
    ],
    [
        sg.Button("Submit"), sg.Button("Clear")
    ]
]

return_viewer = [
    [
        sg.Text('Recommendation:')
    ],
    [
        sg.Output(size=(50,4), key='-OUTPUT-')
    ],
    [
        sg.Push(), sg.Button("Exit")
    ]
]

layout = [
    [
        sg.Column(entry_mask),
        sg.VSeperator(),
        sg.Column(return_viewer)
    ]
]

window = sg.Window("CAD Lite Recommendations", layout)

win2_active = False
while True:
    event, values = window.read()
    response_plans = import_response_plans()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Submit":
        call_type = values["-CALL TYPE-"]
        grid = values["-GRID-"]
        recommendation = get_recommendations(call_type, grid)
        print(recommendation)
    if event == "Clear":
        window['-CALL TYPE-'].update("")
        window['-GRID-'].update("")
        window['-OUTPUT-'].update("")
window.close()