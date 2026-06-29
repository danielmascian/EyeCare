from tkinter import *
from tkinter import ttk
from timer import Timer

root = Tk()
root.title("Eyecare")
root.geometry('350x350')
root.resizable(width=True,height = True)

frm = ttk.Frame(root)
frm.pack()

info_frame = ttk.Frame(frm)
info_frame.grid(row=0, column=0)

button_info_frame = ttk.LabelFrame(frm,text = "Buttons")
button_info_frame.grid(row = 2,column = 0,padx = 20,pady =20)

input_frame = ttk.Frame(frm)
input_frame.grid(row=1, column=0)

timer_label = ttk.Label(info_frame, text="Minutes: 0, Seconds: 0")
timer_label.grid(column=0, row=0)

timer = Timer(root, timer_label)
input_seconds = ttk.Entry(input_frame)
input_seconds.grid(column = 0 , row = 1)

ttk.Button(button_info_frame,text="Start",command=lambda: timer.start(int(input_seconds.get()))).grid(column=1, row=1)
ttk.Button(button_info_frame,text="Stop",command=timer.stop).grid(column=1, row=2)
ttk.Button(button_info_frame,text="Quit",command=root.destroy).grid(column=1, row=3)

root.mainloop()