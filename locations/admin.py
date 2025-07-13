from django.contrib import admin
from .models import Country, Province, City, Location
# Register your models here.

admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Location)
