import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

auth_form = tk.Tk()
auth_form.geometry('400x600')

form_x, form_y = 30, 30
entry_width = 20

auth = [{'login': 'admin', 'password': 'admin'}]

def autentication():
    login = log.get()
    password = pas.get()
    for user in auth:
        if login == user['login'] and password == user['password']:
            auth_form.withdraw()
            admin_form.deiconify()
            return
    showerror('эээээээ','НЕПРАВИЛЬНО ДОН')

tk.Label(text='Логин').place(x=form_x, y=form_y)
log = tk.Entry(width=entry_width)
log.place(x=form_x, y=form_y + 30)

tk.Label(text='Пароль').place(x=form_x, y=form_y + 60)
pas = tk.Entry( width=entry_width)
pas.place(x=form_x, y=form_y + 90)

tk.Button(text='Войти', width=entry_width, command=autentication).place(x=form_x, y=form_y + 120)


admin_form = tk.Tk()
admin_form.geometry('1900x900+0+0')

tickets = []

def add_tickets():
    ticket = []
    ticket.append(article.get())
    ticket.append(datetime.datetime.now())
    ticket.append(typee.get())
    ticket.append(modele.get())
    ticket.append(problem.get())
    ticket.append(fio.get())
    ticket.append(number.get())
    ticket.append(status.get())

    tickets.append(ticket)
    showinfo('', '')
    print_tickets()

def print_tickets():
    tree.delete(*tree.get_children())
    for ticket in tickets:
        tree.insert('', 'end', values=ticket)

def select():
    ticket_id = article.get()
    for ticket in tickets:
        if ticket[0] == ticket_id:
            ticket[2] = typee.get()
            ticket[3] = modele.get()
            ticket[4] = problem.get()
            ticket[5] = fio.get()
            ticket[6] = number.get()
            ticket[7] = status.get()
            break
    showinfo('','')
    print_tickets()

tk.Label(admin_form, text='Номер заявки').place(x=form_x, y=form_y + 60)
article = tk.Entry(admin_form, width=entry_width)
article.place(x=form_x, y=form_y + 90)

tk.Label(admin_form, text='Вид оргтехники').place(x=form_x, y=form_y + 120)
typee = tk.Entry(admin_form, width=entry_width)
typee.place(x=form_x, y=form_y + 150)

tk.Label(admin_form, text='Модель').place(x=form_x, y=form_y + 180)
modele = tk.Entry(admin_form, width=entry_width)
modele.place(x=form_x, y=form_y + 210)

tk.Label(admin_form, text='Описание проблемы').place(x=form_x, y=form_y + 240)
problem = tk.Entry(admin_form, width=entry_width)
problem.place(x=form_x, y=form_y + 270)

tk.Label(admin_form, text='ФИО клиента').place(x=form_x, y=form_y + 300)
fio = tk.Entry(admin_form, width=entry_width)
fio.place(x=form_x, y=form_y + 330)

tk.Label(admin_form, text='Номер телефона').place(x=form_x, y=form_y + 360)
number = tk.Entry(admin_form, width=entry_width)
number.place(x=form_x, y=form_y + 390)

tk.Label(admin_form, text='Статус заявки').place(x=form_x, y=form_y + 420)
status = ttk.Combobox(admin_form, width=entry_width, values=['Новая заявка', 'Впроцессе ремонта', 'Завершена'])
status.current(0)
status.place(x=form_x, y=form_y + 450)

tk.Button(admin_form, text='Записать', width=entry_width, command=add_tickets).place(x=form_x, y=form_y + 480)
tk.Button(admin_form, text='Изменить', width=entry_width, command=select).place(x=form_x, y=form_y + 510)

columns = ['Номер заявки',
           'Дата добавления',
           'Вид оргтехники',
           'Модель',
           'Описание проблемы',
           'ФИО клиента',
           'Номер телефона',
           'Статус заявки'
           ]

tree = ttk.Treeview(admin_form, columns=columns, show='headings', height=10)
for i in columns:
    tree.heading(i, text=i)
tree.place(x=250, y=50)

admin_form.withdraw()
auth_form.mainloop()
