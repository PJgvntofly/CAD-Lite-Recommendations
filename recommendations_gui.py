#Create GUI for CAD Lite Recommendations

import PySimpleGUI as sg
from get_recommendations import get_recommendations

menu_def = [
        ['File', ['Exit']],
        ['Admin', ['View FRLs', 'Update FRLs']]
    ]

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
        sg.Button("Exit")
    ]
]

layout = [
    [
        sg.MenuBar(menu_def)
    ],
    [
        sg.Column(entry_mask),
        sg.VSeperator(),
        sg.Column(return_viewer)
    ]
]

window = sg.Window("CAD Lite Recommendations", layout)

while True:
    event, values = window.read()
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
    if event == 'View FRLs':
        layout2 = [
            [
                sg.Text("Select the Agency:"),
                sg.DropDown()
            ]
        ]
        window_2 = sg.Window("Admin Panel", layout2)
window.close()