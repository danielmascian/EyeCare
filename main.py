from tkinter import *
from tkinter import ttk
from timer import Timer

root = Tk()
root.title("Eyecare")

frm = ttk.Frame(root, padding=10)
frm.grid()

timer_label = ttk.Label(frm, text="Minutes: 0, Seconds: 0")
timer_label.grid(column=0, row=1)

timer = Timer(root, timer_label)

ttk.Label(frm, text="Eyecare").grid(column=0, row=0)

ttk.Button(frm,text="Timer Start",command=lambda: timer.start(100)).grid(column=1, row=0)

ttk.Button(frm,text="Timer Stop",command=timer.stop).grid(column=2, row=0)

ttk.Button(frm,text="Quit",command=root.destroy).grid(column=3, row=0)

root.mainloop()