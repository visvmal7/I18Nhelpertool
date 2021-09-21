from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.template.loader import get_template
from django.template import Context, loader
from django.views.generic.base import TemplateView
from django.utils import timezone
from django.shortcuts import redirect
from django.core import serializers
from .models import VehicleBrand
from django import template
from django import forms
from django.template import RequestContext
from django.core.urlresolvers import reverse
from subprocess import check_output
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
import os
import sys, subprocess, shlex
import ftplib

import django_tables2 as tables
from django.db.models import Q
import datetime
import time
import bz2
import base64
import os
import webbrowser
import urllib


# Import tables from models
from .models import Line
from .models import Post
from .forms import PostForm
from .forms import SearchForm
from .forms import SetLocaleForm
from .forms import SysLocaleForm
from .forms import nbusetupForm
from .forms import OSDownloadForm

from .models import NBUList
from .models import RD
from .models import RDProtocol
from .models import TokenNumberNew
from .models import VehicleBrand
from .models import VehicleModel
from .forms import UploadFileForm
from .models import NbuModel

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Document
from .models import NbuModel

register = template.Library()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# list of mobile User Agents
mobile_uas = [
    'w3c ', 'acs-', 'alav', 'alca', 'amoi', 'audi', 'avan', 'benq', 'bird', 'blac',
    'blaz', 'brew', 'cell', 'cldc', 'cmd-', 'dang', 'doco', 'eric', 'hipt', 'inno',
    'ipaq', 'java', 'jigs', 'kddi', 'keji', 'leno', 'lg-c', 'lg-d', 'lg-g', 'lge-',
    'maui', 'maxo', 'midp', 'mits', 'mmef', 'mobi', 'mot-', 'moto', 'mwbp', 'nec-',
    'newt', 'noki', 'oper', 'palm', 'pana', 'pant', 'phil', 'play', 'port', 'prox',
    'qwap', 'sage', 'sams', 'sany', 'sch-', 'sec-', 'send', 'seri', 'sgh-', 'shar',
    'sie-', 'siem', 'smal', 'smar', 'sony', 'sph-', 'symb', 't-mo', 'teli', 'tim-',
    'tosh', 'tsm-', 'upg1', 'upsi', 'vk-v', 'voda', 'wap-', 'wapa', 'wapi', 'wapp',
    'wapr', 'webc', 'winw', 'winw', 'xda', 'xda-'
]

mobile_ua_hints = ['SymbianOS', 'Opera Mini', 'iPhone']


def mobileBrowser(request):
    ''' Super simple device detection, returns True for mobile devices '''

    # print ("Request format:+++++")
    # print (request.META)
    # print ("\n")

    mobile_browser = False

    # Original code for user agent checking
    # ua = request.META['HTTP_USER_AGENT'].lower()[0:4]

    ua = request.META['HTTP_USER_AGENT'].lower()

    print("User agent:::::::::::")
    print(ua)
    print("\n")

    if ("android" in ua) and ("windows" not in ua):
        print("Request from Android device...\n")
        mobile_browser = True
    elif "iemobile" in ua:
        print("Request from  Windows mobile device...\n")
        mobile_browser = True
    else:
        print("mobile_browser - false - line 77\n")
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                # print ("mobile_brower - else hints - line 69\nhint = ")
                # print (hint)
                mobile_browser = True
            else:
                print("mobile_ua - else hint - line 73\nhint = ")
    return mobile_browser


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# @register.inclusion_tag("brand_model_select.html")
@register.inclusion_tag("nbusearch.html")
def brand_model_select():
    brand_list = VehicleBrand.objects.all()
    return {'brand_list': brand_list}


def all_json_models(request, brand):
    current_brand = VehicleBrand.objects.get(code=brand)
    models = VehicleModel.objects.all().filter(brand=current_brand)
    json_models = serializers.serialize("json", models)
    return HttpResponse(json_models, mimetype="application/javascript")


# ------------- Working code with NBUList DB--------------
# def nbucompdbview(request):
#     '''A view to send user to the tables page'''
#     # Display full table of NBU Compatibility to chose from
#     nbucompquery_results = NBUList.objects.all()
#     return render(request, 'smartapp/nbucompdb.html', {'nbucomplist': nbucompquery_results})
# ----------------------------------------------------------
def handle_uploaded_file(file):
    # with open('some/file/name.txt', 'r+') as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)
    # file = open("Sample.log", "r+")
    wordcount = {}
    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    for k, v in wordcount.items():
        # print (k, v)
        print(str(bz2.decompress(base64.b64decode(bytes(k, encoding='utf-8')))).split('+'), v)
    file.close();


# ----------------------------------------------------------
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('smartapp/nbucompdb.html')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


# ----------------------------------------------------------
def nbucompdbview(request):
    '''A view to send user to the tables page'''
    # Display full table of NBU Compatibility to chose from
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('smartapp/nbucompdb.html')
    else:
        form = UploadFileForm()

    # nbucompquery_results = RD.objects.all()
    # return render(request, 'smartapp/nbucompdb.html', {'nbucomplist': nbucompquery_results})
    nbucompquery_results = "Page development in progress..."
    return render(request, 'smartapp/nbucompdb.html', {'nbucomplist': nbucompquery_results})


# ----------------------------------------------------------
class ResultsTable(tables.Table):
    Product_Name = tables.Column()
    Application_Name = tables.Column()
    Storage_Type = tables.Column()
    Version = tables.Column()
    Protocol = tables.Column()

    class Meta:
        attrs = {"class": "paleblue"}  # This is important for nice table display


# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

# Manual Download page
def syslocaledownload(request):
    name = "Manual Download Page"
    return render_to_response('smartapp/syslocaledownload.html', {'name': name})

def pythondate(event):
    webbrowser.open_new("https://confluence.community.veritas.com/display/GLOB/Locale")



# Setup Locale page
def setuplocale(request):
    name = "Locale Setup Page"
    print(name)
    '''A view to send user to the tables page'''
    # If the form has been submitted...
    if request.method == 'POST':
        # A form bound to the POST data that has fields for user name and user password

        form = SetLocaleForm(request.POST, request.FILES)
        print("Checking if Form is valid..\n")

        # All validation rules pass
        if form.is_valid():
            print("===================\n")
            print("Form is valid...\n")
            print("Fetching the results...")

            print("Selected platform_name is:")
            platformname = form.cleaned_data['platform_name']
            print(platformname)

            machinename = form.cleaned_data['machine_name']
            print("machine_name string:")
            print(machinename)

            username = form.cleaned_data['user_name']
            print("function_name string:")
            print(username)

            remotepasswd = form.cleaned_data['remote_passwd']
            print("remotepasswd string:")
            print(remotepasswd)

            langchoice = form.cleaned_data['lang_choice']
            print("langchoice string:")
            print(langchoice)

            ctext = "Locale setup successful on " + machinename
            print("-----ctext-----")
            print(ctext)

            # Formatting the commands
            jap_lang = "ja_JP.utf8"
            eng_lang = "en_US.utf8"
            chin_lang = "zh_CN.utf8"
            fre_lang = "fr_FR.utf8"
            
            cmd1 = ("echo y | C:\\plink\\plink.exe -ssh -v " + username + "@" + machinename + " -pw " + remotepasswd + " wget http://10.210.151.11/static/SysLocale.sh")
            cmd2 = ("echo y | C:\\plink\\plink.exe -ssh -v " + username + "@" + machinename + " -pw " + remotepasswd + " chmod +x /root/SysLocale.sh")
            cmd3 = ("echo y | C:\\plink\\plink.exe -ssh -t " + username + "@" + machinename + " -pw " + remotepasswd +  " /root/SysLocale.sh " )
			
            if 10 == int(platformname):
                print("Selected Linux Platform")
                if 1 == int(langchoice):
                    ctext = ('Japanese setup done on Linux platform, machine: ') + machinename
                    print(ctext)
                    print("Executing cmd1...")
                    print(cmd1)
                    os.system(cmd1)
                    print("Executing cmd2 ...")
                    print(cmd2)
                    os.system(cmd2)
                    print("Executing cmd3...")
                    print ("value of ctext" + ctext)

                    os.system(cmd3 + jap_lang)

                   
                elif 2 == int(langchoice):
                    ctext = ('English setup done on Linux platform, machine: ') + machinename
                    print(ctext)
                    print("Executing...")
                    print(cmd1)
                    os.system(cmd1)
                    print("Executing...")
                    print(cmd2)
                    os.system(cmd2)
                    print("Executing...")
                    print(cmd3)
                    os.system(cmd3 + eng_lang)
                    #subprocess.call("sh /root/SysLocale.sh"  + eng_lang, shell=True)

                elif 3 == int(langchoice):
                    ctext = ('Simplified Chinese setup done on Linux platform, machine: ') + machinename
                    print(ctext)
                    print("Executing...")
                    print(cmd1)
                    os.system(cmd1)
                    print("Executing...")
                    print(cmd2)
                    os.system(cmd2)
                    print("Executing...")
                    print(cmd3)
                    os.system(cmd3 + chin_lang)

                elif 4 == int(langchoice):
                    ctext = ('French setup done on Linux platform, machine: ') + machinename
                    print(ctext)
                    print("Executing...")
                    print(cmd1)
                    os.system(cmd1)
                    print("Executing...")
                    print(cmd2)
                    os.system(cmd2)
                    print("Executing...")
                    print(cmd3)
                    os.system(cmd3 + fre_lang)
                else:
                    print(ctext)

            elif 20 == int(platformname):
                print("Selected Windows Platform")
                if 1 == int(langchoice):
                    ctext = ('Setting up Japanese on Windows platform, machine: ') + machinename
                    print(ctext)

                elif 2 == int(langchoice):
                    ctext = ('Setting up English on Windows platform, machine: ') + machinename
                    print(ctext)

                elif 3 == int(langchoice):
                    ctext = ('Setting up Simplified Windows on Linux platform, machine: ') + machinename
                    print(ctext)

                elif 4 == int(langchoice):
                    ctext = ('Setting up French on Windows platform, machine: ') + machinename
                    print(ctext)
                else:
                    print(ctext)

            else:
                print("Selected Future Platform")
                
            # filename = "Under construction..."
            print("Debug - 1")
            filename = ""
            return render(request, 'smartapp/nbu_result.html', {'nbucomp_got': ctext, 'testvar': filename})

        else:


            cachequery_results = NBUList.objects.all()
            print("For some reason form is invalid, please continue debugging...\n")
            return render(request, 'smartapp/setuplocale.html', {'racache': cachequery_results})
    elif request.method == 'GET':
        # print("GET method invoked by default... You nailed it...")
        cachequery_results = NBUList.objects.all()
        if mobileBrowser(request):
            print("Inside mobile GET request...####354")
            t = loader.get_template('smartapp/m_home.html')
            return render(request, 'smartapp/setuplocale.html', {'racache': cachequery_results})
        else:
            return render(request, 'smartapp/setuplocale.html', {'racache': cachequery_results})
    else:
        # Need to add code for GET request here:
        # I dont know what is default for this else:(
        cachequery_results = NBUList.objects.all()
        # return render(request, 'smartapp/setuplocale.html', {'racache': cachequery_results})
        if mobileBrowser(request):
            print("Inside mobile home request... Line 264")
            t = loader.get_template('smartapp/m_home.html')
            return render(request, 'smartapp/setuplocale.html', {'racache': cachequery_results})
        else:
            return render(request, 'smartapp/setuplocale.html', {'racache': cachequery_results})

# Setup Locale page
def syslocaleform(request):
    name = "Locale Setup Page"
    print(name)
    '''A view to send user to the tables page'''
    # If the form has been submitted...
    if request.method == 'POST':
        # A form bound to the POST data that has fields for user name and user password

        form = SysLocaleForm(request.POST, request.FILES)
        print("Checking if Form is valid..\n")

        # All validation rules pass
        if form.is_valid():
            print("===================\n")
            print("Form is valid...\n")
            print("Fetching the results...")

            print("Selected Enter_character is:")
            entercharacter = form.cleaned_data['Enter_character']
            print(entercharacter)

            localedate = form.cleaned_data['Locale_Date']
            print("Locale_Date string:")
            print(localedate)

            utcdate = form.cleaned_data['UTC_Date']
            print("UTC_Date string:")
            print(utcdate)

            localetime = form.cleaned_data['Locale_Time']
            print("Locale_Time string:")
            print(localetime)

            selectlang = form.cleaned_data['select_lang']
            print("select_lang string:")
            print(selectlang)

            ctext = "Successful  "
            print("-----ctext---    --")
            print(ctext)

           # filename = "Under construction..."
            filename = ""
            return render(request, 'smartapp/nbu_result.html', {'nbucomp_got': ctext, 'testvar': filename})

        else:

            cachequery_results = NBUList.objects.all()
            print("For some reason form is invalid, please continue debugging...\n")
            return render(request, 'smartapp/nbucompdb.html', {'racache': cachequery_results})
    elif request.method == 'GET':
        # print("GET method invoked by default... You nailed it...")
        cachequery_results = NBUList.objects.all()
        if mobileBrowser(request):
            print("Inside mobile GET request...####354")
            t = loader.get_template('smartapp/m_home.html')
            return render(request, 'smartapp/nbucompdb.html', {'racache': cachequery_results})
        else:
            return render(request, 'smartapp/nbucompdb.html', {'racache': cachequery_results})
    else:
        # Need to add code for GET request here:
        # I dont know what is default for this else:(
        cachequery_results = NBUList.objects.all()
        # return render(request, 'smartapp/nbucompdb.html', {'racache': cachequery_results})
        if mobileBrowser(request):
            print("Inside mobile home request... Line 264")
            t = loader.get_template('smartapp/m_home.html')
            return render(request, 'smartapp/nbucompdb.html', {'racache': cachequery_results})
        else:
            return render(request, 'smartapp/nbucompdb.html', {'racache': cachequery_results})

#For in/unstall lanuage pack
def nbusetup(request):
    name = "Manual Download Page"
    return render_to_response('smartapp/nbucompdb.htm', {'name': name})
'''
    name = " Language pack Install and uninstall Page"
    print(name)
    #A view to send user to the tables page
    # If the form has been submitted...
    if request.method == 'POST':
        # A form bound to the POST data that has fields for user name and user password
        form = nbusetupForm(request.POST, request.FILES)
        print("Checking if Form is valid..\n")

        # All validation rules pass
        if form.is_valid():
            print("===================\n")
            print("Form is valid...\n")
            print("Fetching the results...")

            nbuinst_uninst = form.cleaned_data['nbuinst_uninst']
            print("inst_uninst string:")
            print(nbuinst_uninst)

            print("Selected platform_name is:")
            nbuplatform_name = form.cleaned_data['nbuplatform_name']
            print(nbuplatform_name)

            nbumachinename = form.cleaned_data['nbumachine_name']
            print("machine_name string:")
            print(nbumachinename)

            nbuusername = form.cleaned_data['nbumachine_username']
            print("function_name string:")
            print(nbuusername)

            nburemotepasswd = form.cleaned_data['nbumachine_password']
            print("remotepasswd string:")
            print(nburemotepasswd)

            nbubuildver = form.cleaned_data['nbubuild_ver']
            print("buildver string:")
            print(nbubuildver)

            nbulangchoice = form.cleaned_data['nbulang_pack']
            print("langchoice string:")
            print(nbulangchoice)

            ctext = "Locale setup successful on " + nbumachinename
            print("-----ctext-----")
            print(ctext)

            jap_lag = "ja_JP.UTF-8"
            eng_lang = "en_US.UTF-8"
            chin_lang = "zh_CN.UTF-8"
            fre_lang = "fr_FR.UTF-8"

            cmd1 = ("C:\\plink\\plink.exe -v " + nbuusername + "@" + nbumachinename + " -pw " + nburemotepasswd + " wget http://10.209.179.18:8000/static/SysLocale.sh")
            cmd2 = ("C:\\plink\\plink.exe -v " + nbuusername + "@" + nbumachinename + " -pw " + nburemotepasswd + " chmod +x /root/SysLocale.sh")
            cmd3 = ("C:\\plink\\plink.exe -v " + nbuusername + "@" + nbumachinename + " -pw " + nburemotepasswd + " /root/SysLocale.sh ")

            ##if 101 == int(nbuinst_uninst):
              ##  print ("You selected option for installation")
            if 10 == int(nbuplatform_name):
                print("Selected Linux Platform")
             ##if 10 == int(platformname):
                
                if 1 == int(langchoice):
                    ctext = ('Setting up Japanese on Linux platform, machine: ') + nbumachinename
                    print(ctext)
                    print("Executing...")
                    print(cmd1)
                    os.system(cmd1)
                    print("Executing...")
                    print(cmd2)
                    os.system(cmd2)
                    print("Executing...")
                    print(cmd3)
                    os.system(cmd3 + jap_lag)

                elif 2 == int(langchoice):
                    ctext = ('Setting up English on Linux platform, machine: ') + nbumachinename
                    print(ctext)
                    print("Executing...")
                    print(cmd1)
                    os.system(cmd1)
                    print("Executing...")
                    print(cmd2)
                    os.system(cmd2)
                    print("Executing...")
                    print(cmd3)
                    os.system(cmd3 + eng_lang)

                elif 3 == int(langchoice):
                    ctext = ('Setting up Simplified Chinese on Linux platform, machine: ') + nbumachinename
                    print(ctext)
                    print("Executing...")
                    print(cmd1)
                    os.system(cmd1)
                    print("Executing...")
                    print(cmd2)
                    os.system(cmd2)
                    print("Executing...")
                    print(cmd3)
                    os.system(cmd3 + chin_lang)

                elif 4 == int(langchoice):
                    ctext = ('Setting up French on Linux platform, machine: ') + nbumachinename
                    print(ctext)
                    print("Executing...")
                    print(cmd1)
                    os.system(cmd1)
                    print("Executing...")
                    print(cmd2)
                    os.system(cmd2)
                    print("Executing...")
                    print(cmd3)
                    os.system(cmd3 + fre_lang)
                else:
                    print(ctext)

            elif 20 == int(nbuplatform_name):
                    print("Selected Windows Platform")
                    if 1 == int(nbulangchoice):
                        ctext = ('Setting up Japanese on Windows platform, machine: ') + nbumachinename
                        print(ctext)

                    elif 2 == int(nbulangchoice):
                        ctext = ('Setting up English on Windows platform, machine: ') + nbumachinename
                        print(ctext)

                    elif 3 == int(nbulangchoice):
                        ctext = ('Setting up Simplified Windows on Linux platform, machine: ') + nbumachinename
                        print(ctext)

                    elif 4 == int(nbulangchoice):
                        ctext = ('Setting up French on Windows platform, machine: ') + nbumachinename
                        print(ctext)
                    else:
                        print(ctext)
            else:
                    print("Selected Future Platform")
           # elif 102 == int(nbuinst_uninst):
            #    print ("You selected option for uninstallation")
            #else:
             #   print("Selected Future Platform")
            # filename = "Under construction..."
            filename = ""
            return render(request, 'smartapp/nbu_result.html', {'nbucomp_got': ctext, 'testvar': filename})
        else:
            cachequery_results = NBUList.objects.all()
            print("For some reason form is invalid, please continue debugging...\n")
            return render(request, 'smartapp/nbusetup.html', {'racache': cachequery_results})
    elif request.method == 'GET':
        # print("GET method invoked by default... You nailed it...")
        cachequery_results = NBUList.objects.all()
        if mobileBrowser(request):
            print("Inside mobile GET request...####354")
            t = loader.get_template('smartapp/m_home.html')
            return render(request, 'smartapp/nbusetup.html', {'racache': cachequery_results})
        else:
            return render(request, 'smartapp/nbusetup.html', {'racache': cachequery_results})

    else:
        # Need to add code for GET request here:
        # I dont know what is default for this else:(
        cachequery_results = NBUList.objects.all()
        #return render(request, 'smartapp/nbusetup.html', {'racache': cachequery_results})

        if mobileBrowser(request):
            print("Inside mobile home request... Line 264")
            t = loader.get_template('smartapp/m_home.html')
            return render(request, 'smartapp/nbusetup.html', {'racache': cachequery_results})
        else:
            return render(request, 'smartapp/nbusetup.html', {'racache': cachequery_results})


'''
def i18nhome(request):
    name = "Manual Download Page"
    return render_to_response('smartapp/i18nhome.html', {'name': name})

def osdownload(request):

    name = " Language pack Download OS Page"
    print(name)

    #A view to send user to the tables page
    # If the form has been submitted...
    if request.method == 'POST':
        # A form bound to the POST data that has fields for user name and user password
        form = OSDownloadForm(request.POST, request.FILES)
        print("Checking if Form is valid..\n")

        # All validation rules pass
        if form.is_valid():
            print("===================\n")
            print("Form is valid...\n")
            print("Fetching the results...")

            print("Selected continent is:")
            continentname = form.cleaned_data['continent']
            print("continet string:")
                                    
            countryname = form.cleaned_data['country']
            print("country string:")
            print(countryname)

            ctext = "OS download successfully done "
            print("-----ctext-----")
            print(ctext)

            ftp = ftplib.FTP("10.210.76.61")
            ftp.login("repouser", "repouser")
            ftp.cwd("/binary/I18N/OS")
            ftp.retrlines("LIST")
            
        
            ftp.cwd(continentname)
            ftp.retrlines("LIST")

            # Stores the Files and folder in array
            listing = []
            store_list = []
            ftp.retrlines("LIST", listing.append)
            i=0
            while i < len(listing):
                words = listing[i].split(None, 8)
                found_filename = words[-1].lstrip()
                store_list.append(found_filename)
                print (store_list)
                i += 1
            #ISOname = input(countryname)

            # validates if files or folder user wants is available
            if countryname in store_list:
                user_location = "C:\\projects\\internationalization\\smartapp\\static\\os"
                local_filename = os.path.join(os.getcwd(), user_location, countryname)
                print("this is the location", local_filename)
                gFile = open(local_filename, "wb")
                ftp.retrbinary('RETR %s' %countryname, gFile.write)
                gFile.close()
                ftp.quit()
             
            else:
                print (countryname,"you are searching is not available")
                quit()          
            filename = ""
            return render(request, 'smartapp/nbu_result.html', {'nbucomp_got': ctext, 'testvar': filename})
        else:
            cachequery_results = NBUList.objects.all()
            print("For some reason form is invalid, please continue debugging...\n")
            return render(request, 'smartapp/osdownload.html', {'racache': cachequery_results})
    elif request.method == 'GET':
        # print("GET method invoked by default... You nailed it...")
        cachequery_results = NBUList.objects.all()
        if mobileBrowser(request):
            print("Inside mobile GET request...####354")
            t = loader.get_template('smartapp/m_home.html')
            return render(request, 'smartapp/osdownload.html', {'racache': cachequery_results})
        else:
            return render(request, 'smartapp/osdownload.html', {'racache': cachequery_results})

    else:
        # Need to add code for GET request here:
        # I dont know what is default for this else:(
        cachequery_results = NBUList.objects.all()
        #return render(request, 'smartapp/osdownload.html', {'racache': cachequery_results})

        if mobileBrowser(request):
            print("Inside mobile home request... Line 264")
            t = loader.get_template('smartapp/m_home.html')
            return render(request, 'smartapp/osdownload.html', {'racache': cachequery_results})
        else:
            return render(request, 'smartapp/osdownload.html', {'racache': cachequery_results})

def nbucompsearch(request):

    '''A view to send user to the tables page'''
    # If the form has been submitted...
    if request.method == 'POST':
        # A form bound to the POST data that has fields for user name and user password

        form = SearchForm(request.POST, request.FILES)
        print("Checking if Form is valid..\n")

        # filename1 = ''

        # All validation rules pass
        if form.is_valid():
            print("===================\n")
            print("Form is valid...\n")
            print("Fetching the results...")

            print("Selected Platoform is:")
            functionname = form.cleaned_data['function_name']
            print(functionname)

            ctext = ""
            filename = ""
            print("-----ctext-----")
            print(ctext)

           
            return render(request, 'smartapp/nbu_result.html', {'nbucomp_got': ctext, 'testvar': filename})

        else:
            cachequery_results = NBUList.objects.all()
            print("For some reason form is invalid, please continue debugging...\n")
            return render(request, 'smartapp/nbusearch.html', {'racache': cachequery_results})
    elif request.method == 'GET':
        # print("GET method invoked by default... You nailed it...")
        cachequery_results = NBUList.objects.all()
        if mobileBrowser(request):
            print("Inside mobile GET request... Line 273")
            t = loader.get_template('smartapp/m_home.html')
            return render(request, 'smartapp/m_nbusearch.html', {'racache': cachequery_results})
        else:
            return render(request, 'smartapp/nbusearch.html', {'racache': cachequery_results})
    else:
        # Need to add code for GET request here:
        # I dont know what is default for this else:(
        cachequery_results = NBUList.objects.all()
        # return render(request, 'smartapp/nbusearch.html', {'racache': cachequery_results})
        if mobileBrowser(request):
            print("Inside mobile home request... Line 264")
            t = loader.get_template('smartapp/m_home.html')
            return render(request, 'smartapp/m_nbusearch.html', {'racache': cachequery_results})
        else:
            return render(request, 'smartapp/nbusearch.html', {'racache': cachequery_results})


# Create your views here.
# Home page will give login page to user
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
    # return HttpResponse("Hello World!")
    # return render_to_response("smartapp/home.html", {'hello' : "Welcome to S.M.A.R.T."})
    # Last working:
    # return render_to_response("smartapp/home.html", {'lines': Line.objects.all()})
    print("Inside home request... Line 262")
    if mobileBrowser(request):
        print("Inside mobile home request... Line 264")
        t = loader.get_template('smartapp/m_home.html')
    else:
        print("Inside Desktop home request... Line 267")
        t = loader.get_template('smartapp/home.html')

    c = Context({})  # normally your page data would go here

    return HttpResponse(t.render(c))


def smartapp(request):
    # return HttpResponse("Hello World!")
    # return render_to_response("smartapp/home.html", {'hello' : "Welcome to S.M.A.R.T."})
    name = "Pranav"
    t = get_template('smartapp/home.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)


def smartapp_simple(request):
    # return HttpResponse("Hello World!")
    # return render_to_response("smartapp/home.html", {'hello' : "Welcome to S.M.A.R.T."})
    name = "Pranav Sahasrabudhe"
    return render_to_response('home.html', {'name': name})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'smartapp/post_list.html', {'posts': posts})


class SmartTemplate(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(SmartTemplate, self).get_context_data(**kwargs)
        context['name'] = 'PranavS'
        return context


def post_detail(request):
    return render(request, 'smartapp/post_edit.html', {'form': form})


def failview(request):
    '''A view to send user to the fail page if he enters the wrong airport codes'''
    # org working::::
    return render(request, 'smartapp/fail.html')


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'smartapp/post_edit.html', {'form': form})
