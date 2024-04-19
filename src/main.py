from datetime import datetime
import time
import tkinter as tk

from src.fibonacciclock import FibonacciClock
from src.fibonaccigui import FibonacciClockGUI


def task_1():
    # initialize clock object
    clock = FibonacciClock()
    # main loop
    while True:
        # get current time
        now = datetime.now()
        # update colors according to time
        clock.update_colors(now)
        print("Current time: ", now.strftime("%H:%M"))
        print("Fibonacci Clock simulation: ", clock.get_time_representation(), clock.get_colors())
        time.sleep(300)


def task_2():
    root = tk.Tk()
    app = FibonacciClockGUI(root)
    root.mainloop()


def main():
    # task_1()
    task_2()


if __name__ == "__main__":
    main()
