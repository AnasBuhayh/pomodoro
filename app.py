from tkinter import *
import time


class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init__window()

        self.remaining = 0
        self.sessions = 1

        self.countdownLabel = Label(self, text="", width=10, height=5)
        self.countdownLabel.pack()
        
        self.startButton = Button(self, text="Start", command= lambda: self.countdown(10))
        self.startButton.pack()

    def init__window(self):
        self.master.title("Pomodoro")
        self.pack(fill=BOTH, expand=1)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.countdownLabel.configure(text="time's up!")

        else:
            mins, secs = divmod(self.remaining, 60)
            timer = '{:02}:{:02d}'.format(mins, secs)
            self.countdownLabel.configure(text=timer)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)


root = Tk()
root.geometry("300x600")
app = Window(root)

root.mainloop()