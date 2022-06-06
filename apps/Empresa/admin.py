from django.contrib import admin
from .models import Sede, Dependencia, sedeDependencia
# Register your models here.
admin.site.register(Sede)
admin.site.register(Dependencia)
admin.site.register(sedeDependencia)