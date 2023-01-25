import tkinter as tk
from tkinter import *
import subprocess


window_main = tk.Tk(className='WhatsApp-Send To Number', )
window_main.geometry("400x200")

Label(window_main, text="Masukkan Nomornya").pack(padx=20, pady=10)

entry_1 = tk.StringVar()

entry_widget_1 = tk.Entry(window_main, textvariable=entry_1)
entry_widget_1.pack(padx=20, pady=10)

def submitValues():
    num = entry_1.get()
    number=""
    if num[:3] == "+62":
        number = num[4:]
    elif num[0] == "0":
        number = num[1:]
    elif num[:2] == "62":
        number = num[2:]
    
    subprocess.Popen(["cmd", "/C", f"start whatsapp://send?phone=62{number}"], shell=True)

submit = tk.Button(window_main, text="SEND TO", command=submitValues)
submit.pack(padx=20, pady=10)

window_main.mainloop()