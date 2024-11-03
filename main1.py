from tkinter import *

#Tk themed widget set (Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton, Scale and Scrollbar)
from tkinter.ttk import *

#creating tkinter window
root=Tk()
root.title('menu')

#creating menubar
menubar = Menu(root)

#a tearoff permits you to detach menus for the most wiundow making floating menus
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='file', menu=file)
file.add_command(label='new file', command = None)
file.add_command(label='open...', command = None)
file.add_command(label='save', command = None)
file.add_separator()
file.add_command(label='exit', command = root.destroy)



edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='edit', menu = edit)
edit.add_command(label='undo', command = None)
edit.add_command(label='redo', command = None)
edit.add_separator()
edit.add_command(label='cut', command = None)
edit.add_command(label='copy', command = None)
edit.add_command(label='paste', command = None)
edit.add_separator()
edit.add_command(label='find', command = None)
edit.add_command(label='replace', command = None)
edit.add_separator()
edit.add_command(label='find in files', command = None)
edit.add_command(label='replace in files', command = None)

help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label='help', menu = help)
help.add_command(label='tk help', command = None)
help.add_command(label='demo', command = None)
help.add_separator()
help.add_command(label='about', command = root.destroy)

#display menu
root.config(menu=menubar)
root.mainloop()