from django.contrib import admin
from .models import Line
from .models import Post
from .models import NBUList
from .models import VehicleBrand
from .models import VehicleModel
from .models import RD
from .models import RDProtocol
from .models import TokenNumberNew

# Register your models here.
from smartapp.models import NbuModel

admin.site.register(Post)
admin.site.register(Line)
admin.site.register(NBUList)
admin.site.register(RDProtocol)
admin.site.register(RD)

admin.site.register(TokenNumberNew)
admin.site.register(VehicleBrand)
admin.site.register(VehicleModel)
admin.site.register(NbuModel)


class MyModelAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/admin/my_own_admin.js',)
        css = {
            'all': ('css/blog.css',)
        }
