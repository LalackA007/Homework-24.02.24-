import tkinter.messagebox
from tkinter import *
import random

root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f'450x200+{int(w / 2) - 225}+{int(h / 2) - 100}')

random_num = None
n = 1


def generate():
    global random_num
    try:
        poch = int(ent_min.get())
        kin = int(ent_max.get())
        if poch > kin:
            tkinter.messagebox.showwarning('Зауваження', 'Потрібно ввести спершу менше, '
                                                         'а потім більше ціле число')
        else:
            random_num = random.randint(poch, kin)
            btn_gen['state'] = 'disabled'
            ent_min['state'] = 'disabled'
            ent_max['state'] = 'disabled'
            ent_start['state'] = 'normal'
            btn_start['state'] = 'normal'
            lab_start.place(x=20, y=130)
            ent_start.place(x=180, y=130)
            btn_start.place(x=320, y=120)
            frame = Frame(root, height=2, bd=1, relief=SUNKEN)
            frame.pack(fill=X, padx=10, pady=97)
    except ValueError:
        tkinter.messagebox.showerror('Помилка', 'Потрібно ввести цілі числа')


def start():
    global random_num
    global n
    try:
        root.title(f'Спроба №{n}')
        ch = int(ent_start.get())
        if ch > int(random_num):
            tkinter.messagebox.showinfo('Не вгадав', 'Згадане число менше')
            n += 1
        elif ch < int(random_num):
            tkinter.messagebox.showinfo('Не вгадав', 'Згадане число більше')
            n += 1
        elif ch == random_num:
            rez = tkinter.messagebox.askyesno('Ви перемогли!', 'Грати ще раз?')
            if rez:
                ent_start.delete(0, END)
                btn_gen['state'] = 'normal'
                ent_min['state'] = 'normal'
                ent_max['state'] = 'normal'
                ent_min.delete(0, END)
                ent_max.delete(0, END)
                ent_start['state'] = 'disabled'
                btn_start['state'] = 'disabled'
                root.title(':)')
                generate()
                n = 1
            else:
                root.quit()
        if n > 5:
            res = tkinter.messagebox.askyesno('Ви програли!', 'Ваші спроби закінчилися. Бажаєте грати ще раз?')
            if res:
                ent_start.delete(0, END)
                btn_gen['state'] = 'normal'
                ent_min['state'] = 'normal'
                ent_max['state'] = 'normal'
                ent_min.delete(0, END)
                ent_max.delete(0, END)
                ent_start['state'] = 'disabled'
                btn_start['state'] = 'disabled'
                root.title(':)')
                generate()
                n = 1
            else:
                root.quit()
    except ValueError:
        tkinter.messagebox.showerror('Помилка', 'Потрібно ввести цілі числа')


Label(root, text='Min number', font=(None, 14)).place(x=20, y=15)
Label(root, text='Max number', font=(None, 14)).place(x=20, y=50)

ent_min = Entry(root, width=10, font=(None, 14))
ent_min.place(x=150, y=15)

ent_max = Entry(root, width=10, font=(None, 14))
ent_max.place(x=150, y=50)

btn_gen = Button(root, text='Generate', width=10, height=2, command=generate)
btn_gen.place(x=320, y=25)

# ///////////////////////////////////////////////////////////////////////////////////////

lab_start = Label(root, text='Вгадайте число', font=(None, 14))
lab_start.place_forget()

ent_start = Entry(root, width=10, font=(None, 14))
ent_start.place_forget()

btn_start = Button(root, text='Вгадати', width=10, height=2, command=start)
btn_start.place_forget()

root.mainloop()
