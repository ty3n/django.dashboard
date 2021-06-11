from django.contrib import admin
from .models import Line, Region, Station, Upload
# Register your models here.
admin.site.register(Line)
admin.site.register(Region)
admin.site.register(Station)
admin.site.register(Upload)