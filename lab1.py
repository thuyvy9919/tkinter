# Trương Thị Thùy Vy 
#  43.01.104.210
import tkinter as tk
from tkinter import messagebox

def load():
    messagebox.showinfo('Đây là thông tin của bạn ', message='Tên : ' + entName.get() +'\n'+ 'Số điện thoại : ' + entPhone.get())
    
vip = tk.Tk()

#title
vip.title("Hello Everyone")

#label
tk.Label(vip, text = 'Name', font = 'Times 20 bold').grid(row = 0, column = 0, ipadx = 20, ipady = 20)
tk.Label(vip, text = 'Phone', font = 'Times 20 bold').grid(row = 1, column = 0, ipadx = 20, ipady = 20)

#entry
entName = tk.Entry(vip, font = 'Times 20 bold')
entName.grid(row = 0, column = 1)
entPhone = tk.Entry(vip, font = 'Times 20 bold')
entPhone.grid(row = 1, column = 1)

#button
btnEnter = tk.Button(vip, text = 'Enter', bg = '#b7b7a4', font = 'Times 30 bold italic', command = load).grid(row = 2, columnspan = 2)
vip.geometry('500x500')

tk.mainloop()
