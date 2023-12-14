#Create GUI for CAD Lite Recommendations

import PySimpleGUI as sg
from get_recommendations import get_recommendations

sg.theme('DarkBlack1')
sg.set_global_icon('SNO911-Logo.ico')

#Create etext boxes for users to enter the call type and grid plus a submit button
def create_entry_mask():
    return [
        [sg.Text("Call Type:"), sg.Push(), sg.In(size=(15,1), key="-CALL TYPE-")],
        [sg.Text("Grid:"), sg.Push(), sg.In(size=(15,1), key="-GRID-")],
        [sg.Button("Submit",bind_return_key=True), sg.Button("Clear")]
    ]

#Create window for viewing output
def create_return_viewer():
    return [
        [sg.Text('Recommendation:')],
        [sg.Output(size=(50,5), key='-OUTPUT-')],
        [sg.Push(), sg.Button("Exit")]
    ]

def main():
    entry_mask = create_entry_mask()
    return_viewer = create_return_viewer()
    layout = [
        [sg.Titlebar(title='CAD Lite Recommendations')],
        [sg.Column(entry_mask), sg.VSeperator(), sg.Column(return_viewer)]
    ]

    window = sg.Window("CAD Lite Recommendations", layout, no_titlebar=False, finalize=True, font='Courier 14', grab_anywhere=True, keep_on_top=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Submit":
            call_type = values["-CALL TYPE-"]
            grid = values["-GRID-"]
            recommendation = get_recommendations(call_type, grid, window)
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

if __name__ == "__main__":
    main()