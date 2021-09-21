# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

def index(Request):
    return HttpResponse("<h2>Welcome to Globalization world!!!</h2>")
from django.shortcuts import render

# Create your views here.
