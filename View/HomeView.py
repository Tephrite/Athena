#!/usr/bin/env python3.6
from Model.Speech import *

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk


    py3 = 0
except ImportError:
    import tkinter.ttk as ttk

    py3 = 1

font24 = "-family {Tw Cen MT Condensed Extra Bold} -size 24 "  \
        "-weight normal -slant roman -underline 0 -overstrike 0"

class Athena(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.wm_title(self, "Athena")
        Tk.wm_iconbitmap(self, "D:\\Programming\\Python Projects\\Athena\\Images\\logo.ico")

        # Windowed

        Tk.wm_geometry(self, "1920x1080")
        Tk.wm_resizable(self, 0, 0)

        # Fullscreen
        """
        self.overrideredirect(1)
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w,h))
        """

        frame = Frame(self)
        frame.tkraise()
        frame.pack()

        self.canvas = Canvas(self, width=1920, height=1080)
        self.canvas.pack(expand=YES, fill=BOTH)

        self.iBackground = PhotoImage(file="D:\Programming\Python Projects\Athena\Images\BackgroundFull.png")
        self.canvas.create_image(0,0, image=self.iBackground, anchor = NW)

        self.tText = self.canvas.create_text(900, 900, text="", font=font24, fill="#c0c0c0", anchor=N)

        self.bButton = Button(self, text="Activate", command=self.getSpeech, anchor=W)
        self.bButton.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        self.bButton_window = self.canvas.create_window(900, 1000, anchor=NW, window=self.bButton)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def vp_start_gui():
        '''Starting point when module is the main routine.'''
        global app

        app = Athena()
        app.mainloop()

    def getSpeech(self):
        speech = Speech()
        speech.getSpeech(self)




