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
            jap_lag = "ja_JP.UTF-8"
            chin_lang = "zh_CN.UTF-8"
            eng_lang = "en_US.UTF-8"
            fre_lang = "fr_FR.UTF-8"

            cmd1 = (
                "C:\\plink\\plink.exe -v " + username + "@" + machinename + " -pw " + remotepasswd + " wget http://10.209.179.18:8000/static/SysLocale.sh")
            cmd2 = (
                "C:\\plink\\plink.exe -v " + username + "@" + machinename + " -pw " + remotepasswd + " chmod +x /root/SysLocale.sh")
            cmd3 = (
                "C:\\plink\\plink.exe -v " + username + "@" + machinename + " -pw " + remotepasswd + " /root/SysLocale.sh ")

            if 10 == int(platformname):
                print("Selected Linux Platform")
                if 1 == int(langchoice):
                    ctext = ('Setting up Japanese on Linux platform, machine: ') + machinename
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
                    ctext = ('Setting up English on Linux platform, machine: ') + machinename
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
                    ctext = ('Setting up Simplified Chinese on Linux platform, machine: ') + machinename
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
                    ctext = ('Setting up French on Linux platform, machine: ') + machinename
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
