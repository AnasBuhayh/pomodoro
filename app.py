from tkinter import *
from functools import partial
import time


class Window(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.init__window()

        self.SettingsWorkTime = 5
        self.SettingsRestTime = 3
        self.SettingsSessions = 3

        self.remainingWork = 5
        self.remainingRest = 3
        self.remainingSessions = 3
        self.remaining = 0

        self.current = None

        self.current_activity = Label(self, text="", width=10, height=5)
        self.current_activity.pack()

        self.countdownLabel = Label(self, text="", width=10, height=5)
        self.countdownLabel.pack()

        self.startButton = Button(self, text="Start", command= partial(self.sessionsCountdown))
        self.startButton.pack()

        self.sessionLabel = Label(self, text="", width=10, height=5)
        self.sessionLabel.pack()

    def init__window(self):
        self.master.title("Pomodoro")
        self.pack(fill=BOTH, expand=1)

    def newWorkSession(self):
        return

    def sessionsCountdown(self):
        self.sessionLabel.config(text=str(self.remainingSessions))
        if self.remainingSessions <= 0:
            self.current_activity.config(text="Done!")
            self.countdownLabel.configure(text="time's up!")
            self.restParameters()
            return 

        if self.current == "working":
            self.current = 'resting'
            self.current_activity.config(text="Resting:")
            self.remainingRest = 3
            self.remainingSessions -= 1
        else:
            self.current = 'working'
            self.current_activity.config(text="Working:")
            self.remainingWork = 5

        if self.current == "working":
            self.remaining = self.remainingWork
        else:
            self.remaining = self.remainingRest
        self.countdown()
          
    def countdown(self):
        if self.remaining <= 0:
            self.sessionsCountdown()

        else:
            mins, secs = divmod(self.remaining, 60)
            timer = '{:02}:{:02d}'.format(mins, secs)
            self.countdownLabel.configure(text=timer)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
    
    def restParameters(self):
        self.remainingWork = self.SettingsWorkTime
        self.remainingRest = self.SettingsWorkTime
        self.remainingSessions = self.SettingsSessions 

root = Tk()
root.geometry("300x600")
app = Window(root)

root.mainloop()