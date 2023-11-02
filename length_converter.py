import PySimpleGUI as sg

label1 = sg.Text("Enter Feet: ")
input_feet = sg.InputText(key='f')
label2 = sg.Text("Enter inches: ")
input_inches = sg.InputText(key='i')
m = 0
label_m = sg.Text(f"Meters: {m} ", key='mts')
convert_button = sg.Button("Convert", key='cb')

window = sg.Window("Converter", layout=[[label1, input_feet],
                                        [label2, input_inches],
                                        [convert_button, label_m]])
while True:
    event, values = window.read()
    match event:
        case 'cb':
            m = ((int(values['f'])*12)+int(values['i']))*0.0254
            window['mts'].update(value=f"Meters: {m} ")
        case sg.WIN_CLOSED:
            break
window.close()
