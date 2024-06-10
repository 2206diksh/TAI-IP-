import tkinter as tk
from datetime import datetime, timedelta
import time

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        
        # Title Label
        self.title_label = tk.Label(master, text="Countdown Timer", font=("Helvetica", 24))
        self.title_label.pack(pady=20)
        
        # Time Entry
        self.time_entry_label = tk.Label(master, text="Enter time in seconds:")
        self.time_entry_label.pack()
        
        self.time_entry = tk.Entry(master, width=10)
        self.time_entry.pack(pady=5)
        
        # Start Button
        self.start_button = tk.Button(master, text="Start", command=self.start_countdown)
        self.start_button.pack(pady=20)
        
        # Countdown Display
        self.countdown_label = tk.Label(master, text="", font=("Helvetica", 48))
        self.countdown_label.pack(pady=20)
        
        self.time_left = 0
    
    def start_countdown(self):
        try:
            self.time_left = int(self.time_entry.get())
            self.update_timer()
        except ValueError:
            self.countdown_label.config(text="Invalid Input")
    
    def update_timer(self):
        if self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            hours, mins = divmod(mins, 60)
            time_format = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            self.countdown_label.config(text=time_format)
            self.time_left -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.countdown_label.config(text="Time's up!")

if __name__ == "__main__":
    root = tk.Tk()
    countdown_timer = CountdownTimer(root)
    root.mainloop()
