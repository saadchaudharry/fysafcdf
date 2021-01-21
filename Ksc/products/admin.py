from django.contrib import admin
from .models import Catagory,Prod,Contactus

# Register your models here.

class Prodadmin(admin.ModelAdmin):
    list_display = ['__str__','catagory']
    class Meta:
        model=Prod

admin.site.register(Catagory)
admin.site.register(Prod,Prodadmin)
admin.site.register(Contactus)

