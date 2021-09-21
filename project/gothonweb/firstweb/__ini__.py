
from flask import Flask, render_template,request, flash
from Tkinter import *
import datetime
import locale
import sys

app = Flask(__name__)

@app.route("/home/")
def home():
     return render_template('home.html')


@app.route('/I18NDate/')
def I18NDate():
    locale.setlocale(locale.LC_ALL, '')
    format_ = datetime.datetime.today().strftime('%x')
    DateFormat = format_.decode(locale.getlocale()[1])
    return DateFormat

if __name__ == '__main__':
    app.run(debug=True)


#https://www.tutorialspoint.com/flask/flask_quick_guide.htm



