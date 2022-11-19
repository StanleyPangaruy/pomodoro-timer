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

        self.root.mainloop()

pomodoroTimer()


