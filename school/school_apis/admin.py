from django.contrib import admin
from .models import Students, Rooms, Teachers 
# Register your models here.

admin.site.register(Students)
admin.site.register(Rooms)
admin.site.register(Teachers)
