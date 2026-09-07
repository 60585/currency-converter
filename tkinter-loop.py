from tkinter import *
import tkinter as tk

window = tk.Tk()
window.geometry("600x400")

name_var=tk.StringVar()
passw_var=tk.StringVar()

def convert():
    pounds = float(txt_pounds.get())
    euros = pounds * 1.17
    
    txt_euros.delete(0, tk.END)
    txt_euros.insert(0, euros)
    

LBL_pounds = tk.Label(window, text="Pounds")
LBL_pounds.pack()

txt_pounds = tk.Entry(window, width = 15)
txt_pounds.pack()

btn_convert = Button(window, text="Convert", command=convert)
btn_convert.pack(pady = 10)

LBL_euros = Label(window, text="Euros")
LBL_euros.pack()

txt_euros = Entry(window, width = 15)
txt_euros.pack()

window.mainloop()

