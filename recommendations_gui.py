#Create GUI for CAD Lite Recommendations

import PySimpleGUI as sg
from get_recommendations import get_recommendations

sg.theme('DarkBlack1')
sg.set_global_icon('SNO911-Logo.ico')

#Create etext boxes for users to enter the call type and grid plus a submit button
def create_entry_mask():
    return [
        [sg.Text("Call Type:"), sg.Push(), sg.In(size=(15,1), key="-CALL TYPE-"), sg.Push()],
        [sg.Text("Grid:     "), sg.Push(), sg.In(size=(15,1), key="-GRID-"), sg.Push()],
        [sg.Button("Submit",bind_return_key=True), sg.Button("Clear"), sg.Push(), sg.Button("Additional Requests")]
    ]

#Create window for viewing output
def create_return_viewer():
    return [
        [sg.Text('Recommendation:')],
        [sg.Output(size=(50,5), key='-OUTPUT-')],
        [sg.Button('Recommendations Help'),sg.Push(), sg.Button("Exit")]
    ]

def open_help_screen():
    tips_layout = [
        [sg.Text("If you receive an error saying that the Grid isn't supported,")],
        [sg.Text("try the next closest Grid based on the CAD Lite map")]
    ]
    unit_layout = [
        [sg.Text("To add the closest unit for a given unit type,")],
        [sg.Text("click the 'Additional Requests' button then select")],
        [sg.Text("the desired unit type from the given options. Enter")],
        [sg.Text("the grid of the incident and hit submit. A recommendation")],
        [sg.Text("for just that unit type will be returned.")]
    ]
    help_layout = [
        [sg.Frame('Troubleshooting Tips', tips_layout)],
        [sg.Frame("Adding a Unit", unit_layout)],
        [sg.Push(), sg.Button("Close")]
    ]
    window = sg.Window("Recommendations Help", help_layout, modal=False, font='Courier 14')
    while True:
        event, values = window.read()
        if event == "Close" or event == sg.WIN_CLOSED:
            break
    window.close()

def open_additional_requests():
    rb = []
    rb.append(sg.Radio("Engine", "units", key="engine", enable_events=True))
    rb.append(sg.Radio("Ladder", "units", key="ladder", enable_events=True))
    rb.append(sg.Radio("Aid Unit", "units", key="aid", enable_events=True))
    rb.append(sg.Radio("Medic Unit", "units", key="medic", enable_events=True))
    rb.append(sg.Radio("Command Unit", "units", key="command", enable_events=True))
    rb.append(sg.Radio("Brush Truck", "units", key="brush", enable_events=True))
    rb.append(sg.Radio("Tender", "units", key="tender", enable_events=True))
    unit_frame = sg.Frame("Unit Type", [rb])
    layout = [
        [unit_frame],
        [[sg.Text("Grid:  "),sg.In(size=(15,1), key="-GRID-")]],
        [sg.Button("Submit",bind_return_key=True), sg.Button("Clear"), sg.Push(), sg.Button('Close')]
    ]
    window = sg.Window("Additional Requests", layout, modal=True, font='Courier 14')
    while True:
        event, values = window.read()
        if event == 'Close' or event == sg.WIN_CLOSED:
            break
        if event == 'engine':
            call_type = 'engine'
        if event == 'ladder':
            call_type = 'ladder'
        if event == 'aid':
            call_type = 'aid unit'
        if event == 'medic':
            call_type = 'medic unit'
        if event == 'command':
            call_type = 'command unit'
        if event == 'brush':
            call_type = 'brush truck'
        if event == 'tender':
            call_type = 'tender'
        if event == 'Submit':
            grid = values["-GRID-"]
            recommendation = get_recommendations(call_type, grid, window)
            print(recommendation)
            break
    window.close()

def main():
    entry_mask = create_entry_mask()
    return_viewer = create_return_viewer()
    layout = [
        #[sg.Titlebar(title='CAD Lite Recommendations')],
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
        if event == "Recommendations Help":
            window.keep_on_top_clear()
            open_help_screen()
            window.keep_on_top_set()
        if event == "Additional Requests":
            window.keep_on_top_clear()
            open_additional_requests()
            window.keep_on_top_set()
    window.close()

if __name__ == "__main__":
    main()