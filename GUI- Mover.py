from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import os
import shutil

root = Tk()
root.title('Vimart-Bulk Mover 1.0')
root.resizable(0,0)


def direct():
    if os.path.isfile(file_path.get()):
        l = filedialog.askdirectory(title='Move files to', initialdir=file_path.get())
    else:
        l = filedialog.askdirectory(title='Move files to', initialdir=os.path.expanduser('~'))
        file_path.delete(0,END)
        file_path.insert(0,l)

    folder_path.set(l)
    lista= os.listdir(l)
    exty = ['All files', 'All Filers and Folders']
    for e in lista:
        if os.path.isfile(f'{l}/{e}'):
            h = os.path.splitext(e)[1]
            if h not in exty:
                exty.append(h)

    ext_choosen['values'] = tuple(exty)


def move_to():
    if os.path.isfile(file_path_to.get()):
        t = filedialog.askdirectory(title='Move files to', initialdir=file_path_to.get())
    else:
        t = filedialog.askdirectory(title='Move files to', initialdir=os.path.expanduser('~'))
        file_path_to.delete(0, END)
        file_path_to.insert(0, t)

    folder_tom.set(t)


def move():
    ext_file= ext_choosen.get()
    folder_from = folder_path.get()
    folder_to = folder_tom.get()

    # ------------
    files_list = os.listdir(folder_from)
    if ext_file == 'All files':
        for file in files_list:
            if os.path.isfile(f'{folder_from}/{file}'):
                shutil.move(f'{folder_from}/{file}', folder_to)
    elif ext_file == 'All Filers and Folders':
        for file in files_list:
            shutil.move(f'{folder_from}/{file}', folder_to)
    else:
        for file in files_list:
            if os.path.isfile(f'{folder_from}/{file}'):
                if file.endswith(ext_file):
                    shutil.move(f'{folder_from}/{file}', folder_to)
    mb.showinfo('Succes', f'Objects moved from: {folder_from} to {folder_to}')


def moveq():
    print(f'to:{len(folder_tom.get())} From:{len(folder_path.get())} Ext: {len(ext_choosen.get())}')
    if len(ext_choosen.get()) < 1 or len(folder_path.get()) < 1 or len(folder_tom.get()) < 1:
        mb.showerror('not ext', 'You\'ve select Source, Target moving and Extensions. ')
        return
    if mb.askyesno('sure?', f'Want to move {ext_choosen.get()} to {folder_tom.get()}'):
        move()
    else:
        mb.showinfo('No', 'Moving has been cancelled')


movefrom = Label(text='Move From: ')
movefrom.grid(column=0, row=0)

file_path = Entry(width=30)
file_path.grid(column=1,row=0)

butonem = Button(text='Directory', command=direct, fg='orange', bg='#0f2a52', highlightthickness=0)
butonem.grid(column=2, row=0)
folder_path = StringVar()
folder_tom = StringVar()
print('first>',folder_path.get())
print('first',len((folder_path.get())))
b = Label(text='')
b.grid(column=1, row=1)
po = []
pliki=[]
bgs=Button(text="Vimart 1.0\n Bulk File Mover",
          background = '#0f2a52', foreground ="orange",
          font = ("Times New Roman", 15, 'bold')).grid(column=1,row=2)

Label(text = "Select extension:").grid(column = 0,row = 3, padx = 10, pady = 25)

kl = StringVar()
ext_choosen = ttk.Combobox(width = 27)
point= ['All files']
ext_choosen['values'] = ()

ext_choosen.grid(column=1, row=3)
ext_choosen.current()

# ----------------- Move to ---------------#
moveto = Label(text=' Move To: ')
moveto.grid(column=0, row=4)
file_path_to = Entry(width=30)
file_path_to.grid(column=1,row=4)
butone_to = Button(text='Directory', command=move_to, bg='#0f2a52',fg='orange', highlightthickness=-1)
butone_to.grid(column=2, row=4)
def ent(e):
    butone_to['background'] = '#0f2a52'
def leave(e):
    butone_to['background']='#0f2a52'
butone_to.bind('<Enter>', ent)
butone_to.bind('<Leave>', leave)
c = Label(text='')
c.grid(column=1, row=5)

Button(text='Move', command= moveq).grid(column=1, row=6)

root.mainloop()
