
            # Formatting the commands
            jap_lag = "JA"
            chin_lang = "ZH"
            eng_lang = "EN"
            fre_lang = "FR"

            cmd1 = (
                "C:\\plink\\plink.exe -v " + username + "@" + machinename + " -pw " + remotepasswd + " wget http://10.209.179.18:8000/static/nbulp.sh")
			cmd2 = (
                "C:\\plink\\plink.exe -v " + username + "@" + machinename + " -pw " + remotepasswd + " mkdir /newbuilds")
            cmd3 = (
                "C:\\plink\\plink.exe -v " + username + "@" + machinename + " -pw " + remotepasswd + " chmod +x /newbuilds/nbulp.sh")
            cmd4 = (
                "C:\\plink\\plink.exe -v " + username + "@" + machinename + " -pw " + remotepasswd + " /newbuilds/nbulp.sh ")

            if 10 == int(platformname):
                print("Selected Linux Platform")
				 if 101 == int (inst_uninst)
					print("Selected to install Languagepack ")
					if 1 == int(langchoice):
						ctext = ('Installing Japanese on Linux platform, machine: ') + machinename
						print(ctext)
						print("Executing...")
						print(cmd1)
						os.system(cmd1)
						print("Executing...")
						print(cmd2)
						os.system(cmd2)
						print("Executing...")
						print(cmd3)
						os.system(cmd3 + buildver, jap_lag)

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
						os.system(cmd3 + buildver, eng_lang)

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
						os.system(cmd3 + buildver, chin_lang)

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
						os.system(cmd3 + buildver, fre_lang)
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