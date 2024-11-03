from django.contrib import admin
from .models import Programmer, Error, Fix

admin.site.register(Programmer)
admin.site.register(Error)
admin.site.register(Fix)

