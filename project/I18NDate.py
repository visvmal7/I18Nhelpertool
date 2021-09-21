#!/usr/bin/python
# -*- coding: utf-8 -*-


import datetime
import locale


def I18NDateFind():
    locale.setlocale(locale.LC_ALL, '')
    #print locale.setlocale(locale.LC_ALL,'')
    format_ = datetime.datetime.today().strftime('%x')
    DateFormat = format_.decode(locale.getlocale()[1])
    return DateFormat


if __name__ == '__main__':
    print I18NDateFind()