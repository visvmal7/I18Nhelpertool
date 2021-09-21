

import locale
import os
import gettext

# Set up message catalog access
current_locale, encoding = locale.getdefaultlocale()
print current_locale
locale_path = 'locale'

print locale_path

t = gettext.translation('trial',locale_path,[current_locale])
_ = t.ugettext

print _('This message is in the script.')


# webseif for string extranalization reference

'''https://pymotw.com/2/gettext/
https://stackoverflow.com/questions/31726723/no-translation-file-found-for-domain-django
https: // stackoverflow.com / questions / 3837683 / python - no - translation - file - found -for -domain - using - custom - locale - folder
https://stackoverflow.com/questions/9828629/python-and-gettext'''


# below function is for getting date and time from machine locale


'''import datetime
import locale


print locale.getdefaultlocale()

locale.setlocale(locale.LC_ALL, '')
#print locale.setlocale(locale.LC_ALL,'')
format_ = datetime.datetime.today().strftime('%a, %x %X')
format_u = format_.decode(locale.getlocale()[1])
print format
print format_u'''
