from tkinter import *
from tkinter.ttk import *
import time

root = Tk()
root.title('the deep calls.................')

progress = Progressbar(root, orient = HORIZONTAL, length = 100, mode = 'determinate')
progress.pack(pady=10)

def bar():
    progress['value'] = 20
    #flushes all currently-scheduled idle events from tcl's event queue.
    #idle events are used to postpone processing until "there is nothing else to do"
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 100
    root.update_idletasks()
    time.sleep(1)


stcall = Button(root, text='start the call of the deep...', command = bar).pack(pady=10)
root.mainloop()