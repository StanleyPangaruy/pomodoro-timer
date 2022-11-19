import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

class pomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Pomodo Timer")
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="Tomato.png"))

        self.s = ttk.Style()
        self.s.configure("TNotebook.tab", font = ("Ubuntu", 16))
        self.s.configure("TButton", font = ("Ubuntu", 16))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.pomodoroTimerLabel = ttk.Label(self.tab1, text="25:00", font=("Ubuntu", 48))
        self.pomodoroTimerLabel.pack(pady=20)

        self.shortBreakTimerLabel = ttk.Label(self.tab2, text="5:00", font=("Ubuntu", 48))
        self.shortBreakTimerLabel.pack(pady=20)

        self.longBreakTimerLabel = ttk.Label(self.tab3, text="15:00", font=("Ubuntu", 48))
        self.longBreakTimerLabel.pack(pady=20)

        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")

        self.root.mainloop()

    def startTimerThread(self):
        pass

    def startTimer(self):
        pass

    def resetClock(self):
        pass

    def skipClock(self):
        pass

pomodoroTimer()


