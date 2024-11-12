import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import random

keys = []

#Закрыть окно
def close():
    window.destroy()

#Показать ключ(и)
def show_keys():
    keys_var = StringVar(value=keys)
    listbox = Listbox( listvariable=keys_var)
    listbox.pack(expand=1, fill=BOTH)
    listbox.yview_scroll(number=1, what="units")

#Сгенерировать ключ(и)
def generate():
    p = int(arg_number_of_keys.get())
    for k in range (p + 1):
        alf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
        figure = ['0','1','2','3','4','5','6','7','8','9']
        el0 = []
        el1 = []
        el2 = []
        for i in range(3):
            random_alf = random.choice(alf)
            el0.append(random_alf)
        for j in range(2):
            random_figure = random.choice(figure)
            el0.append(random_figure)
        random.shuffle(el0)

        for i in range(3):
            random_alf = random.choice(alf)
            el1.append(random_alf)
        for j in range(2):
            random_figure = random.choice(figure)
            el1.append(random_figure)
        random.shuffle(el1)

        for i in range(3):
            random_alf = random.choice(alf)
            el2.append(random_alf)
        for j in range(2):
            random_figure = random.choice(figure)
            el2.append(random_figure)
        random.shuffle(el2)

        key = el0 + ['-'] + el1 + ['-'] + el2

        keys.append(''.join(key))
    return keys

#Создание бэкграунда и окна 
window = tk.Tk()
window.geometry('1920x1200')
bg_img = tk.PhotoImage(file='123.png')
lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

#Создание рамки
frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

#Создание заголовка окна
window.title("keygen")

#Number_keys и расположение
lbl_number_keys = tk.Label(frame, text='количество сгенерируемых ключей', font=('Arial', 20), fg='black')
lbl_number_keys.grid(column=0, row=0, padx=0, pady=1, sticky=NW)

#Number_keys и расположение
lbl_number_keys = tk.Label(frame, text='количество сгенерируемых ключей', font=('Arial', 20), fg='black')
lbl_number_keys.grid(column=0, row=0, padx=0, pady=1, sticky=NW)


#Создание окна аргумента number_of_keys
arg_number_of_keys = tk.Entry(frame, width=9)
arg_number_of_keys.insert(0, '')

#Расположение окна аргумента number_of_keys
arg_number_of_keys.grid(column=0, row=1, padx=5, pady=7, sticky=EW)

#Кнопка Generate
btn_generate = tk.Button(frame, text='Generate', command=generate)
btn_generate.grid(column=0, row=2, padx=5, pady=5, sticky=NW)

#Кнопка Cancel
btn_exit = tk.Button(frame, text='Cancel', command=close)
btn_exit.grid(column=0, row=2, padx=75, pady=5, sticky=NW)

#Кнопка show keys
btn_show_keys = tk.Button(frame, text='Show keys', command=show_keys)
btn_show_keys.grid(column=0, row=2, padx=135, pady=5, sticky=NW)


window.mainloop() 