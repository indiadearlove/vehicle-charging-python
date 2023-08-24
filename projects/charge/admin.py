from django.contrib import admin

from projects.charge.models import Vehicle, Charge

admin.site.register(Vehicle)
admin.site.register(Charge)