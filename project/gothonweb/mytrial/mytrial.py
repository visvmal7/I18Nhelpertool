#'A very basic Tkinter example. '''

from Tkinter import *
import webbrowser

def OpenUrl(event):


    webbrowser.open_new("http://www.google.com")

    #webbrowser.open_new(url) \

def OpenUrl1(event):

    webbrowser.open_new("http://www.python.org")

root = Tk()

link = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", OpenUrl)


link1 = Label(root, text="Python Hyperlink", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", OpenUrl1)
root.mainloop()()

