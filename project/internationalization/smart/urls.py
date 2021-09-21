"""smart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from smartapp.views import SmartTemplate
import smartapp.views
from django.conf.urls import include, url

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from smartapp.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', smartapp.views.nbucompsearch, name='home'),
    url(r'^smartapp/$', smartapp.views.smartapp, name='smartapp'),
    url(r'^home/$', smartapp.views.home, name='home'),
    url(r'^post_list/$', smartapp.views.post_list, name='post_list'),
    url(r'^failview/$', smartapp.views.failview, name='failview'),
    url(r'^nbucompdbview/$', smartapp.views.nbucompdbview, name='nbucompdbview'),
    url(r'^i18nkb/$', smartapp.views.nbucompsearch, name='i18nkb'),
    url(r'^syslocaledownload/$', smartapp.views.syslocaledownload, name='syslocaledownload'),
    url(r'^setuplocale/$', smartapp.views.setuplocale, name='setuplocale'),
    url(r'^syslocale/$', smartapp.views.syslocaleform, name='syslocale'),
    url(r'^osdownload/$', smartapp.views.osdownload, name='osdownload'),
    url(r'^i18nhome/$', smartapp.views.i18nhome, name='i18nhome'),
    url(r'^nbusetup/$', smartapp.views.nbusetup, name='nbusetup'),
    url(r'^smartapp_simple/$', smartapp.views.smartapp_simple, name='smartapp_simple'),
    url(r'^smartapp_view/$', SmartTemplate.as_view()),
    url(r'^post/new/$', smartapp.views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/$', smartapp.views.post_detail, name='post_detail'),
    url(r'^brand/', smartapp.views.brand_model_select,name='brand_model_select'),
    url(r'^brand/(?P<brand>[-\w]+)/all_json_models/', smartapp.views.all_json_models,name='all_json_models'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)