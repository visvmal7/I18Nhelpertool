#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *
import os

import subprocess
from subprocess import PIPE,STDOUT, call, check_output
import sys
reload(sys)
sys.setdefaultencoding('utf8')



def Shifton_button():

    ShiftGetLabelchar = Label(text="Enter the characacter here")
    ShiftGetLabelchar.pack()


def select_lang():

    ShiftGetEntry.place(x=330, y=195)
    ShiftGetLabel.place(x=330, y=220)

    Shiftret_char = ShiftGetEntry.get().encode('utf-8')
    ShiftGetValue.set(Shiftret_char)
    print "This is the return value Japanese", Shiftret_char

    global chosen_option
    chosen_option = var.get()

    print chosen_option
    #drop_menu.pack(padx=20, pady=5, anchor=W)
    print "Language selected is :", chosen_option
    if chosen_option == "Japanese":
        print "English"
        os.system("plink -v root@pdqebl21vm5.pne.ven.veritas.com -pw Gyp.s8m /SysLocale.sh ja_JP.UTF-8")
        #os.system("plink -v Shiftret_char -pw Gyp.s8m /SysLocale.sh ja_JP.UTF-8")


class mainpagewidgets:
    def __init__(self, master):

        frame = Frame(master, height=500, width=500, bd=1)
        frame.pack()

        self.mbar = Frame(frame, relief="raised", bd=2)
        self.mbar.pack(fill=X)


        ShiftGetButton = Button(text="Would like to change locale of you machine", command=select_lang)
        ShiftGetButton.pack()



root = Tk()

all = mainpagewidgets(root)
root.title('Internationalization')
root.geometry('500x400')
# This to remove maximize and minimize button
var = StringVar(root)
var.set("Select the language")
OptionMenu(root, var, "ja_JP.UTF-8", "Germany (de)", "France(fr)", command=select_lang)

root.mainloop()

ShiftGetValue=StringVar(root)
ShiftGetEntry = Entry(root)
ShiftGetLabel =Entry(textvariable=ShiftGetValue,bg="grey")




#drop_menu = OptionMenu(root, var, "nglish","Germh)", "Japanese (jp)", "France(fr)", command=grab_and_assign)