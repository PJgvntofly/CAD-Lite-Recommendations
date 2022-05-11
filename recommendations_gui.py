#Create GUI for CAD Lite Recommendations

import PySimpleGUI as sg
from get_recommendations import get_recommendations
from import_response_plans import import_response_plans

sg.theme('DarkBlack1')

entry_mask = [
    [
        sg.Text("Call Type:"),
        sg.Push(),sg.In(size=(15,1), key="-CALL TYPE-")
    ],
    [
        sg.Text("Grid:"),
        sg.Push(), sg.In(size=(15,1), key="-GRID-")
    ],
    [
        sg.Button("Submit",bind_return_key=True), sg.Button("Clear")
    ]
]

return_viewer = [
    [
        sg.Text('Recommendation:')
    ],
    [
        sg.Output(size=(50,5), key='-OUTPUT-')
    ],
    [
        sg.Push(), sg.Button("Exit")
    ]
]

layout = [
    [
        sg.Titlebar(title='CAD Lite Recommendations')
    ],
    [
        sg.Column(entry_mask),
        sg.VSeperator(),
        sg.Column(return_viewer)
    ]
]

window = sg.Window("CAD Lite Recommendations", layout,font='Courier 14')

win2_active = False
while True:
    event, values = window.read()
    response_plans = import_response_plans()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Submit":
        call_type = values["-CALL TYPE-"]
        grid = values["-GRID-"]
        #print(f'Entered Call Type: {call_type.upper()}\nEntered Grid: {grid.upper()}')
        recommendation = get_recommendations(call_type, grid)
        print(recommendation)
        window['-CALL TYPE-'].update("")
        window['-GRID-'].update("")
        window['-CALL TYPE-'].set_focus()
    if event == "Clear":
        window['-CALL TYPE-'].update("")
        window['-GRID-'].update("")
        window['-OUTPUT-'].update("")
        window['-CALL TYPE-'].set_focus()
window.close()