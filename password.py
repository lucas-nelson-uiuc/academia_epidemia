from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from datetime import datetime
import random


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

account_details = {}
with open('accounts.txt', 'r') as accounts_file:
    lines = accounts_file.readlines()
    for line in lines:
        account, password, last_date = line.strip().split('..')
        account_details[account] = (password, last_date)


account_details = {k: v for k, v in sorted(account_details.items(), key=lambda item: item[0].lower())}
accounts = StringVar(value=list(account_details.keys()))

sentmsg = StringVar()
statusmsg = StringVar()

def update_account(*args):
    with open('accounts.txt', 'a+') as file:
        try:
            file.write('{}..{}..{}'.format(
                new_account.get(),
                encrypt_password(new_password.get()),
                datetime.today().date())
                + '\n')
        except:
            Label(c, text='Error adding account').grid(row=1000, column=0)


def delete_account(*args):
    try:
        with open("accounts.txt", "r") as f:
            lines = f.readlines()
        with open("accounts.txt", "w") as f:
            for line in lines:
                if line.strip("\n").split('..')[0] != new_account.get():
                    f.write(line)
    except:
        Label(c, text='Error deleting account').grid(row=1000, column=0)

def last_updated(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        name = list(account_details.keys())[idx]
        date = account_details[name][1]
        statusmsg.set("Last updated: {}".format(date))
    sentmsg.set('')


def encrypt_password(decrypt):
    encrypt = ''
    for i, char in enumerate(decrypt):
        rndm = random.randint(0,1)
        if rndm == 0:
            encrypt += chr(ord(char) + i)
            encrypt += str(rndm)
        if rndm == 1:
            encrypt += chr(ord(char) - i)
            encrypt += str(rndm)
    
    return encrypt


def decrypt_password(encrypt):
    decrypt = ''
    vals = [char for idx, char in enumerate(encrypt) if idx % 2 == 0]
    rnds = [char for idx, char in enumerate(encrypt) if idx % 2 != 0]

    for i, val, rnd in zip(range(len(vals)), vals, rnds):
        if int(rnd) == 0:
            decrypt += chr(ord(val) - i)
        if int(rnd) == 1:
            decrypt += chr(ord(val) + i)

    return decrypt


def show_password(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        real_pw = account_details.get(list(account_details.keys())[idx])[0]
        rael_pw = decrypt_password((real_pw))
        sentmsg.set("Password: {}".format(rael_pw))

a = Frame(root, padx=10, pady=10)
a.grid(column=0, row=0, sticky='nesw')
a.grid_columnconfigure(0, weight=1)
a.grid_rowconfigure(0, weight=1)

b = Frame(root, padx=10, pady=10)
b.grid(column=0, row=1, sticky='nesw')
b.grid_columnconfigure(0, weight=1)
b.grid_rowconfigure(0, weight=1)

c = Frame(root, padx=10, pady=10)
c.grid(column=0, row=2, sticky='nesw')
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(0, weight=1)

iconPath = 'logo.png'
icon = ImageTk.PhotoImage(Image.open(iconPath))
icon_size = Label(a)
icon_size.image = icon
icon_size.configure(image=icon)
icon_size.grid(row=0, column=0, sticky='nesw')

Label(b, text='New Account').grid(row=1, column=0, sticky='e')
Label(b, text='New Password').grid(row=2, column=0, sticky='e')
Label(b, text='Confirm').grid(row=3, column=0, sticky='e')
new_account = Entry(b)
new_password = Entry(b)
Button(b, text='Update', width=11, command=update_account
            ).grid(row=3, column=1, sticky='w')
Button(b, text='Delete', width=11, command=delete_account
            ).grid(row=3, column=1, sticky='e')

lbox = Listbox(c, listvariable=accounts, height=5)
sentlbl = ttk.Label(c, textvariable=sentmsg)
status = ttk.Label(c, textvariable=statusmsg)

new_account.grid(row=1, column=1)
new_password.grid(row=2, column=1)
lbox.grid(column=0, row=100, rowspan=6, sticky='nesw')
sentlbl.grid(column=0, row=107, sticky='ew')
status.grid(column=0, row=106, sticky='ew')
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)

lbox.bind('<<ListboxSelect>>', last_updated)
lbox.bind('<Triple-q>', show_password)

for i in range(0,len(account_details),2):
    lbox.itemconfigure(i, background='#f0f0ff')

sentmsg.set('')
statusmsg.set('')
lbox.selection_set(0)
last_updated()

root.mainloop()