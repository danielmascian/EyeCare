from tkinter import *
from tkinter import ttk
from timer import Timer

root = Tk()
root.title("EyeCare")
root.geometry("400x450")

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

canvas = Canvas(frame, width=220, height=220, highlightthickness=0)
canvas.grid(row=0, column=0)

canvas.create_oval(20, 20, 200, 200, outline="gray80", width=12)

progress = canvas.create_arc(20, 20, 200, 200,start=90,extent=-359,style="arc",outline="#00b050",width=12)

timer_label = ttk.Label(frame, text="Minutes: 0, Seconds: 0", font=("Arial", 14))
timer_label.grid(row=1, column=0, pady=10)

entry = ttk.Entry(frame)
entry.grid(row=2, column=0)

timer = Timer(root, timer_label, canvas, progress)

ttk.Button(frame, text="Start", command=lambda: timer.start(int(entry.get()))).grid(row=3, column=0, pady=5)
ttk.Button(frame, text="Stop", command=timer.stop).grid(row=4, column=0, pady=5)
ttk.Button(frame, text="Quit", command=root.destroy).grid(row=5, column=0, pady=5)

root.mainloop()