#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import locale
import sys


def I18NDateFind():

    locale.setlocale(locale.LC_ALL, '')
    format_ = datetime.datetime.today().strftime('%x')
    DateFormat = format_.decode(locale.getlocale()[1])
    return DateFormat

def I18NTimeFind():

    locale.setlocale(locale.LC_ALL, '')
    format_ = datetime.datetime.today().strftime('%X')
    TimeFormat = format_.decode(locale.getlocale()[1])
    return TimeFormat


def I18NDateTimeFind():
    locale.setlocale(locale.LC_ALL, '')
    format_ = datetime.datetime.today().strftime('%x,%X')
    DateTimeFormat = format_.decode(locale.getlocale()[1])
    return DateTimeFormat

if __name__ == '__main__':

    print I18NDateFind()
    print I18NTimeFind()
    print I18NDateTimeFind()


'''def I18NDateTimeFind():

    try:
        Slocale = raw_input("Enter the country:")
        print "you have enter", Slocale
        if Slocale=='':
            exit()
        else:
            print Slocale
            print "French Date format"

    except:
        locale.setlocale(locale.LC_ALL, '')
        format_ = datetime.datetime.today().strftime('%x')
        DateFormat = format_.decode(locale.getlocale()[1])
        return DateFormat'''

'''def I18NDateTimeFind():

    try:
        Slocale = raw_input("Enter the country:")
        print "Select language number from the list" + "\n" + "1)Chinese (Simplified)_China.936" + "\n" + "2) "
        print "you have enter", Slocale
        if Slocale=='':
            exit()
        else:
            print Slocale
            print "French Date format"

    except:
        locale.setlocale(locale.LC_ALL, '')
        format_ = datetime.datetime.today().strftime('%x')
        DateFormat = format_.decode(locale.getlocale()[1])
        return DateFormat

if __name__ == '__main__':

     #Slocale = 'Chinese (Simplified)_China.936,French_France.1252'

     print "why none", I18NDateTimeFind()'''


# good site for reference of Locale
#http://nullege.com/codes/search/locale.setlocale
#https://www.programcreek.com/python/example/653/locale.LC_ALL
#https: // www.programcreek.com / python / example / 653 / locale.LC_ALL

'''
from __future__ import print_function
import platform
import collections
import pprint


languages = ("chinese, english, french, japanese")

d = collections.defaultdict(list)
t = collections.namedtuple("Locale", "lang setlocale getlocale")
for language in languages.split():
    sloc = locale.setlocale(locale.LC_ALL, language)
    #print "value of sloc", sloc
    gloc = locale.getlocale()
    #print "value of gloc", gloc
    record = t(language, sloc, gloc)
    #print "value of rec", record
    if gloc[0][2]:
       d["windows-like"].append(record)
    else:
        d["unix-like"].append(record)
pprint.pprint(dict(d))'''
