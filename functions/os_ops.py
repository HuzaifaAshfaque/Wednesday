import os 
import subprocess as sp


paths = {
	"notepad":"C:\Windows\system32\\notepad.exe" , 
	"calculator":"C:\\Windows\\System32\\calc.exe",
    "vlc":"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
    "word":"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "powerpoint":"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    "excel":"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    "zoom":"C:\\Users\\DELL\\AppData\\Roaming\\Zoom\\bin\\zoom.exe",
    "cmd":"C:\\Windows\\system32\\cmd.exe",

}

def open_notepad():
    os.startfile(paths['notepad'])

def open_zoom():
    os.startfile(paths["zoom"])

    
def open_excel():
    os.startfile(paths["excel"])


def open_point():
    os.startfile(paths["powerpoint"])


def open_word():
    os.startfile(paths["word"])


def open_vlc():
    os.startfile(paths["vlc"])
#def open_discord():
#    os.startfile(paths['discord'])


def open_cmd():
    # os.system(command= 'start cmd')
    os.startfile(paths['cmd'])


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])