
from Tkinter import *
from PIL import ImageTk, Image
import datetime
import locale
import webbrowser
import subprocess
import codecs
import os
import I18NDate
import gettext
import sys
from subprocess import PIPE, STDOUT, call, pywintypes,check_call
import os
import sys
import paramiko

def Knowledge():
    print "knowledge"


def kn_level1():

    sample.place(x=20, y=100)
    ISO15GetButton.place(x=102, y=100)

def validation():

    print"validation"

def tools():

    print "tools"
def Linux_boot():

    Sys_Mach = LangGetEntryMachine.get().encode('utf-8')
    Sys_user = LangGetEntryuser.get().encode('utf-8')
    Sys_pwd = LangGetEntrypwd.get().encode('utf-8')

    sysmachine.set(Sys_Mach)
    sysuser.set(Sys_user)
    syspwd.set(Sys_pwd)

    print Sys_Mach
    print Sys_user
    print Sys_pwd

    sysuser.set(Sys_user)
    syspwd.set(Sys_pwd)
    print Sys_user
    print Sys_pwd
    Langchosen_option = Langvar.get()

    print "Language selected is are 12356 :", Langchosen_option

    if Langchosen_option == "English":
        print "English"
        os.system("plink -v " + Sys_user + "@" + Sys_Mach + " -pw " + Sys_pwd + " /SysLocale.sh en_US.UTF-8")


def Lang_on_button(event):

    Lang_drop_menu.place(x=20, y=30)
    LangGetButton.place(x=200, y=200)
    LangGetEntryMachine.place(x=170, y=80)
    LangGetEntryuser.place(x=170, y=120)
    LangGetEntrypwd.place(x=170, y=150)
    Langmachinelabel.place(x=50, y=80)
    Languserlabel.place(x=50, y=120)
    Langpwdlabel.place(x=50, y=150)

    Langchosen_option = Langvar.get()
    print "Language selected is are 123 :", Langchosen_option

       #Lang_drop_menu = OptionMenu(root, Langvar, "English", "Germany (de)", "Chinese Simpliefied(zh)", "Japanese (jp)",
     #                           "France(fr)", command=Lang_on_button)


    if Langchosen_option == "English":
        print "English"
        os.system("plink -v " + Sys_user + "@" + Sys_Mach + " -pw " + Sys_pwd + " /SysLocale.sh en_US.UTF-8")
    elif Langchosen_option == "Germany":
        print "Germany (de)"
        os.system("plink -v " + Sys_user + "@" + Sys_Mach + " -pw " + Sys_pwd + " /SysLocale.sh de_DE.UTF-8")
    elif Langchosen_option == "Chinese Simpliefied(zh)":
        print "Chinese Simpliefied(zh)"
        os.system("plink -v " + Sys_user + "@" + Sys_Mach + " -pw " + Sys_pwd + " /SysLocale.sh zh_CN.UTF-8")
    elif Langchosen_option == "France(fr)":
        print "France(fr)"
        os.system("plink -v " + Sys_user + "@" + Sys_Mach + " -pw " + Sys_pwd + " /SysLocale.sh de_DE.UTF-8")
    elif Langchosen_option == "Japanese (jp)":
        print "Japanese (jp)"
        os.system("plink -v " + Sys_user + "@" + Sys_Mach + " -pw " + Sys_pwd + " /SysLocale.sh zh_CN.UTF-8")
    else:
        print "Lang not found"

class mainpagewidgets:
    def __init__(self, master):
        frame = Frame(master, height=500, width=500, bd=1)
        frame.pack()

        self.mbar = Frame(frame, relief="raised", bd=2)
        self.mbar.pack(fill=X)

        # The below details for Confluence links


        # Knowledge References

        self.editbutton = Menubutton(self.mbar, text='      Knowledge       ', )
        self.editbutton.pack(side=LEFT)

        self.editmenu = Menu(self.editbutton, tearoff=0)
        self.editbutton['menu'] = self.editmenu

        self.editmenu.lang = Menu(self.editmenu, tearoff=0)

        self.editmenu.add('command', label='Introduction to I18N',command=Knowledge)

        self.editmenu.add('command', label='Dev Reference', command=Knowledge)

        self.editmenu.add_cascade(label='Levels', menu=self.editmenu.lang)

        self.editmenu.lang.add('command', label='Level 0', command=Knowledge)
        self.editmenu.lang.add('command', label='Level 1', command=kn_level1)
        self.editmenu.lang.add('command', label='Level 2', command=Knowledge)
        self.editmenu.lang.add('command', label='Level 3', command=Knowledge)

        # for Validation reference

        self.viewbutton = Menubutton(self.mbar, text='      Validation  ')
        self.viewbutton.pack(side=LEFT)

        self.viewmenu = Menu(self.viewbutton, tearoff=0)
        self.viewbutton['menu'] = self.viewmenu


        # I18N Tools
        self.toolsbutton = Menubutton(self.mbar, text='         Set locale', )
        self.toolsbutton.pack(side=LEFT)

        self.toolsmenu = Menu(self.toolsbutton, tearoff=0)
        self.toolsbutton['menu'] = self.toolsmenu
        self.toolsmenu.add('command', label='Windows', command=tools)
        self.toolsmenu.add('command', label='Linux', command=Lang_on_button)


root = Tk()

#sample= Label(text="trial")
#ISO15GetButton = Button(text="Would like to validate your Legacy character",command=kn_level1)

Langvar = StringVar(root)
Langvar.set("Select the language")
Lang_drop_menu = OptionMenu(root, Langvar, "English","Germany (de)", "Chinese Simpliefied(zh)", "Japanese (jp)", "France(fr)", command=Lang_on_button)
sysmachine=StringVar(root)
sysuser=StringVar(root)
syspwd=StringVar(root)

LangGetEntryuser = Entry(root)
LangGetEntrypwd = Entry(root)
LangGetEntryMachine = Entry(root)
Languserlabel = Label(text="Enter user name")
Langmachinelabel = Label(text="Enter Machine details")
Langpwdlabel = Label(text="Enter Password")
LangGetButton = Button(text="SUBMIT",command=Linux_boot)
LangGetLabel =Entry(textvariable=sysuser,bg="grey")







all = mainpagewidgets(root)
root.title('Internationalization')
root.geometry('500x400')
# This to remove maximize and minimize button
root.attributes("-toolwindow",1)
root.mainloop()

