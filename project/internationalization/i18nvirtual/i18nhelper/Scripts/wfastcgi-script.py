#!c:\projects\internationalization\i18nvirtual\i18nhelper\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'wfastcgi==3.0.0','console_scripts','wfastcgi'
__requires__ = 'wfastcgi==3.0.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('wfastcgi==3.0.0', 'console_scripts', 'wfastcgi')()
    )
