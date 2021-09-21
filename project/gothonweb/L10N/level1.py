from Tkinter import *


def BackToMain():
    root.destroy()
    from First_GUI import Application
    # from First_GUI import *


def DateFormat(master=None):
    T = Text(master, height=2, width=30)
    T.pack()
    T.insert(INSERT, "This is the solution for Date")


def encoding(master=None):
    T = Text(master, height=2, width=30)
    T.pack()
    T.insert(INSERT, "Tis is the solustion for encoding")


class I18NLevel_1(Frame):
    def Level1Widgets(self, master=None):
        self.Back = Button(master, text="Back to Main", command=self.quit)
        # Commented temporaily for arranding button, Please remove the comment final executiong
        # self.Back = Button(master, text="Back to Main", command=self.BackToMain)
        self.Back["fg"] = "red"
        self.Back.pack(padx=0, pady=01, side=BOTTOM, anchor=W)

        self.I18N_level1 = Button(master, text="I18N Level1", command=DateFormat)
        self.I18N_level1.pack(padx=0, pady=0, side=TOP, anchor=SW)

        self.Dates = Button(master, text="Date Format", command=DateFormat)
        self.Dates.pack(padx=60, pady=1, side=TOP, anchor=SW)

        self.character = Button(master, text="Encoding", command=encoding)
        self.character.pack(padx=60, pady=1, side=TOP, anchor=SW)

        self.number = Button(master, text="Number", command=self.quit)
        self.number.pack(padx=60, pady=1, side=TOP, anchor=SW)

        self.I18N_level2 = Button(master, text="I18N Level2", command=self.quit)
        self.I18N_level2.pack(padx=0, pady=5, anchor=W)
        self.Fonts = Button(master, text="Fonts", command=self.quit)
        self.Fonts.pack(padx=65, pady=1, anchor=W)

        self.strings = Button(master, text="Strings", command=self.quit)
        self.strings.pack(padx=65, pady=1, anchor=W)



        # Below funmction is for Date format, on click of button you will see tehe message

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.Level1Widgets()


root = Tk()
root.title("I18N Level1")
root.geometry("500x400")
L1_app = I18NLevel_1(master=root)
L1_app.mainloop()
root.destroy()


# Nice Link to Layout and other Python UI issue
# http://www.java2s.com/Code/Python/GUI-Tk/LayoutsideTOPLEFT.htm
# http://www.java2s.com/Code/Python/GUI-Tk/LayoutsideTOPLEFT.htm
