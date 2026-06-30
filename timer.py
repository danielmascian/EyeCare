import time


class Timer:
    def __init__(self, root, label, canvas, progress):
        self.root = root
        self.label = label
        self.canvas = canvas
        self.progress = progress

        self.total_time = 0
        self.start_time = 0
        self.timer_id = None

    def start(self, seconds):
        self.stop()

        self.total_time = float(seconds)
        self.start_time = time.perf_counter()

        self.tick()

    def tick(self):
        elapsed = time.perf_counter() - self.start_time
        remaining = max(0, self.total_time - elapsed)

        minutes = int(remaining) // 60
        seconds = int(remaining) % 60

        self.label.config(text=f"Minutes: {minutes}, Seconds: {seconds}")

        percent = remaining / self.total_time if self.total_time > 0 else 0
        angle = -(359 * percent)

        self.canvas.itemconfig(self.progress,extent=angle)

        if remaining > 0:
            self.timer_id = self.root.after(16, self.tick)
        else:
            self.label.config(text="Time is over!")
            self.canvas.itemconfig(self.progress, extent=0)
            self.timer_id = None

    def stop(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        self.label.config(text="Minutes: 0, Seconds: 0")
        self.canvas.itemconfig(self.progress, extent=0)