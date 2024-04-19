import tkinter as tk
from datetime import datetime

from src.fibonacciclock import FibonacciClock


class FibonacciClockGUI:
    def __init__(self, master):
        self.master = master
        master.title("Fibonacci Clock")
        self.canvas = tk.Canvas(master, width=800, height=500, bg="white")
        self.canvas.pack()

        # initialize dict with x, y and size values for blocks
        self.blocks = {
            1: [200, 0, 100],
            11: [300, 0, 100],
            2: [0, 0, 200],
            3: [0, 200, 300],
            5: [300, 0, 500],
        }
        self.fibonacci_values = [1, 1, 2, 3, 5]
        self.clock = FibonacciClock()
        self.render_gui()
        self.update_gui()

    def render_gui(self):
        now = datetime.now()
        self.clock.update_colors(now)
        print("Current time: ", now.strftime("%H:%M"))
        print("Fibonacci Clock simulation: ", self.clock.get_time_representation(), self.clock.colors)
        for i, value in enumerate(self.fibonacci_values):
            x, y, size = self.blocks[value]
            self.canvas.create_rectangle(x, y, x + size, y + size, fill=self.clock.colors[i], outline="black")

    def update_gui(self):
        self.canvas.delete("all")
        self.render_gui()
        # update after 60 sec to ensure smooth transition
        self.master.after(60_000, self.update_gui)


