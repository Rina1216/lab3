import tkinter as tk
from tkinter import messagebox
import random

letters_list = 'abcdefghijklmnopqrstuvwxyz'
numbers_list = '1234567890'


def close():
    window.destroy()

def kayfinder():
    for A1 in mas:
        for B1 in mas:
            for C1 in mas:
                if A1==A and B1==B and C1==C:
                    arg_A.insert(0, A1)
                    arg_B.insert(0, B1)
                    arg_C.insert(0, C1)
                    lbl_result = tk.Label(frame, text='OPEN!!!', font=('Arial', 20))
                    lbl_result.grid(column=2, row=2)
                    break

for letter in range (3):
    code = ''
    for i in range(3):
        code += random.choice(letters_list)
    for i in range(2):
        code += random.choice(numbers_list)
    index_list = '01234'
    for i in range(4):
        a = code[i]
        ramdomindex = int(random.choice(index_list))
        b = code[ramdomindex]
        if i < ramdomindex:
            code = code.replace(b, a, 1)
            code = code.replace(a, b, 1)
        elif i > ramdomindex:
            code = code.replace(a, b, 1)
            code = code.replace(b, a, 1)
    if letter==0:
        A = code
    elif letter==1:
        B = code
    else:
        C = code

mas = []
variable = letters_list + numbers_list
for i in variable:
    for k in variable:
        for p in variable:
            for t in variable:
                for n in variable:
                    s = 0
                    stro = i + k + p + t + n
                    for u in stro:
                        if u in letters_list:
                            s += 1
                    if s == 2:
                        mas.append(stro)

window = tk.Tk()
window.geometry('819x819')
bg_img = tk.PhotoImage(file='donlain.png')

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

lbl_A = tk.Label(frame, text='A', font=('Arial', 200))
lbl_A.grid(column=0, row=0, padx=10, pady=15)
arg_A = tk.Entry(frame, width=20)
arg_A.grid(column=0, row=1, padx=10, pady=15)

lbl_B = tk.Label(frame, text='B', font=('Arial', 200))
lbl_B.grid(column=1, row=0, padx=10, pady=15)
arg_B = tk.Entry(frame, width=20)
arg_B.grid(column=1, row=1, padx=10, pady=15)

lbl_C = tk.Label(frame, text='C', font=('Arial', 200))
lbl_C.grid(column=2, row=0, padx=10, pady=15)
arg_C = tk.Entry(frame, width=20)
arg_C.grid(column=2, row=1, padx=10, pady=15)

lbl_roots = tk.Button(frame, text='open', command=kayfinder)
lbl_roots.grid(column=1, row=2)

window.mainloop()