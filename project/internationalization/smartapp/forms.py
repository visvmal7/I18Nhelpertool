__author__ = 'Pranav.Sahasrabudhe'

from django import forms

from .models import Post
from .models import NBUList
from django.contrib.auth.forms import AuthenticationForm

#from uploads.core.models import Document
from .models import Document
from .models import NbuModel

PRODUCTS = (
    ('NBU', 'NetBackup'),
    ('OPC', 'OpsCenter'),
)

# OST-Vendors

APPLICATION = (
    ('RD', 'Replication Director'),
    ('NDMP', 'Legacy NDMP'),
    ('SNC', 'Snapshot Client'),
    ('CLOUD', 'Cloud'),
    ('OSTV', 'OST-Vendors'),
)

VERSIONS = (
    ('773', '7.7.3'),
    ('772', '7.7.2'),
    ('771', '7.7.1'),
    ('77', '7.7'),
    ('7612', '7.6.1.2'),
    ('7604', '7.6.0.4'),
    ('7507', '7.5.0.7'),
)

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class i18nhome(forms.Form):  # RefactorThis to SetLocaleForm
    ''' Enter_character = forms.CharField(label='Enter_character:', max_length=50, required=True)
     Locale_Date = forms.CharField(label='Regional Date:', max_length=50, required=True)
     UTC_Date = forms.CharField(label='UTC Date:', max_length=50, required=True)
     Locale_Time = forms.CharField(label='Regional Time :', max_length=50, required=True)
     select_lang = forms.CharField(label='select_lang:', max_length=50, required=True)'''

# This is for the setting machine locate
class SetLocaleForm(forms.Form): # RefactorThis to SetLocaleForm
    platform_name = forms.CharField(label='platform name:', max_length=50, required=True)
    machine_name = forms.CharField(label='machine_name:', max_length=50, required=True)
    user_name = forms.CharField(label='user_name:', max_length=50, required=True)
    remote_passwd = forms.CharField(label='remote_passwd:', max_length=50, required=True)
    lang_choice = forms.CharField(label='lang_choice:', max_length=50, required=True)

class OSDownloadForm(forms.Form): # RefactorThis to SetLocaleForm
    continent = forms.CharField(label='continent:', max_length=50, required=True)
    country = forms.CharField(label='country:', max_length=50, required=True)


# this is for NBU Location tab in main page
class SysLocaleForm(forms.Form): # RefactorThis to SetLocaleForm
   ''' Enter_character = forms.CharField(label='Enter_character:', max_length=50, required=True)
    Locale_Date = forms.CharField(label='Regional Date:', max_length=50, required=True)
    UTC_Date = forms.CharField(label='UTC Date:', max_length=50, required=True)
    Locale_Time = forms.CharField(label='Regional Time :', max_length=50, required=True)
    select_lang = forms.CharField(label='select_lang:', max_length=50, required=True)'''




# For installation and uninstallation of NBU
class nbusetupForm(forms.Form): # RefactorThis to NBU Install uninstall
    nbuinst_uninst = forms.CharField(label='nbuinst_uninst:', max_length=50, required=True)
    nbuplatform_name = forms.CharField(label='nbuplatform_name:', max_length=50, required=True)
    nbumachine_name = forms.CharField(label='nbumachine_name:', max_length=50, required=True)
    nbumachine_username = forms.CharField(label='nbumachine_username:', max_length=50, required=True)
    nbumachine_password = forms.CharField(label='nbumachine_password:', max_length=50, required=True)
    nbubuild_ver = forms.CharField(label='nbubuild_ver:', max_length=50, required=True)
    nbulang_pack = forms.CharField(label='nbulang_pack:', max_length=50, required=True)

    #nbusubmit = forms.CharField(label='nbusubmit:', max_length=50, required=True)

class SearchForm(forms.Form):
    function_name = forms.CharField(label='platform name:', max_length=50, required=True)
    # platform_name = forms.CharField(label='platform name:', max_length=50, required=True)
    # machine_name = forms.CharField(label='machine_name:', max_length=50, required=True)
    # user_name = forms.CharField(label='user_name:', max_length=50, required=True)
    # remote_passwd = forms.CharField(label='remote_passwd:', max_length=50, required=True)
    # lang_choice = forms.CharField(label='lang_choice:', max_length=50, required=True)
    # lang_choice
    # remote_passwd

# ------------------------------------
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


# ------------------------------------
class SearchAdvForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # print(
        #     "QlpoOTFBWSZTWauq6ngAAAxfgAgAQAv/8CQAjACq794AIABURQ0xDIAGjQ0Hp6oRT1GyQDQ02iDQAHslVnTIgLZ+dY+sJwhi5qAoyFRQA1lBYTPlSlVy3i/i3M2/dA1yh5p9i0KQs71TRgmE5UkggMPxdyRThQkKuq6ngA==")
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['product_search'] = forms.ChoiceField(choices=PRODUCTS)

    product_search = forms.ChoiceField(choices=PRODUCTS)
    application_search = forms.ChoiceField(choices=APPLICATION, required=True)

    # This was working for text search
    product_search = forms.CharField(label='Product Name:', max_length=50)

    class Meta:
        model = NBUList
        fields = ('product', 'appname', 'storage_name')

        widgets = {
            'product': forms.TextInput(attrs={'placeholder': 'What\'s your name?'}),
            'appname': forms.TextInput(attrs={'placeholder': 'john@example.com'}),
        }


# --------------------------------------------------------------
class RAForm(forms.Form):
    '''A class for a form with search criteria fields'''
    product_search = forms.CharField(max_length=50)
    # --------------------------------------------------------------


class DocumentForm(forms.Form):
    class Meta:
        model = NbuModel
        fields = ('description', 'document',)

    docfile = forms.FileField(
        label='Select a file'
    )
