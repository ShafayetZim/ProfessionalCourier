from django.contrib import admin

from .models import Division, District, Sub, Parcel, Type


admin.site.register(Division)
admin.site.register(District)
admin.site.register(Parcel)
admin.site.register(Sub)
admin.site.register(Type)
