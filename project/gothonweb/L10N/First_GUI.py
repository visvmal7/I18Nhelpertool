from Tkinter import *


def I18NLevel():
    root.destroy()
    from level1 import I18NLevel_1


def say_hi():
    print "hi lets learn Internationaization!"


class Application(Frame):
    def createWidgets(self, master=None):
        self.label = Label(master, text="")
        self.label.pack(side="top", fill='both', expand=True, padx=40, pady=40)

        self.QUIT = Button(master, text="QUIT", command=self.quit)
        self.QUIT["fg"] = "red"
        self.QUIT.pack(padx=5, pady=10, side=LEFT)

        self.I18N_Level = Button(master, text="I18N Level1", command=I18NLevel)
        self.I18N_Level.pack(padx=5, pady=20, side=LEFT)

        ##https://www.python-course.eu/tkinter_layout_management.php alighment link
        self.Dev_Sample = Button(master, text="Code sample", command=say_hi)
        self.Dev_Sample.pack(padx=5, pady=20, side=LEFT)

        self.QA_Sample = Button(master, text="sample for QA", command=say_hi)
        self.QA_Sample.pack(padx=5, pady=20, side=LEFT)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk()
root.title("Internationalization")
root.geometry("500x400")
app = Application(master=root)
app.mainloop()
root.destroy()
