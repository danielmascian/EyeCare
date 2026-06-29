class Timer:
    def __init__(self, root, label):
        self.root = root
        self.label = label
        self.time_left = 0
        self.timer_id = None

    def start(self, seconds):
        self.stop()

        self.time_left = int(seconds)
        self.update_label()
        self.tick()

    def tick(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_label()
            self.timer_id = self.root.after(1000, self.tick)
        else:
            self.label.config(text="Time is over!")
            self.timer_id = None

    def stop(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
            self.label.config(text=f"Minutes: {0}, Seconds: {0}")

    def update_label(self):
        minutes, seconds = divmod(self.time_left, 60)
        self.label.config(text=f"Minutes: {minutes}, Seconds: {seconds}")