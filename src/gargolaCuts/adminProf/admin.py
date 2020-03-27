from django.contrib import admin

# Register your models here.

from .models import Barber, Ads


class barberAdmin(admin.ModelAdmin):
    list_display = ('barberName', 'pub_date')
    search_fields = ['newsTitle']
    list_filter = ['pub_date']
    




class NewsAdmin(admin.ModelAdmin):
    list_display = ('adsTitle', 'pub_date')
    search_fields = ['adsTitle']
    list_filter = ['pub_date']
    
    
admin.site.register(Barber,barberAdmin)
admin.site.register(Ads,NewsAdmin)