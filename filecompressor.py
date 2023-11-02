import PySimpleGUI as sg
from zip_creator import zip_archive
label1 = sg.Text("Select files to Compress")
label2 = sg.Text("Select destination Folder")

file_path = sg.FilesBrowse(key='files')
file_path_text = sg.Input()
destination_path = sg.FolderBrowse(key='dest')
destination_path_text = sg.Input()
compress_button = sg.Button("Compress")
window = sg.Window('File Compressor',
                   layout=[[label1, file_path_text, file_path],
                           [label2, destination_path_text, destination_path],
                           [compress_button]])
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Compress':
            zip_archive(filepaths=values['files'], des=values['dest'])
            pass

window.close()
