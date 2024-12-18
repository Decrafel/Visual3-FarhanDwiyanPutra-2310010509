import PySimpleGUI as sg

window = sg.Window(
    title="Profile", 
    layout=[
        [sg.Text("NPM     :   2310010509", font=("Helvetica", 12))],
        [sg.Text("Nama    :   Farhan Dwiyan Putra", font=("Helvetica", 12))],
        [sg.Text("Kelas   :   5B Non Regular Banjarmasin", font=("Helvetica", 12))],
        [sg.Text("Matkul  :   Pemrograman Visual 3", font=("Helvetica", 12))]
    ],
    size=(400, 200)
)
window()
window.close()
