from django.contrib import admin
from .models import Restaurant, Tag, Preference

# Register your models here.
admin.site.register(Tag)
admin.site.register(Restaurant)
admin.site.register(Preference)