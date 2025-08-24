from django.contrib import admin

from .models import Course, Language, Level

admin.site.register(Course)
admin.site.register(Language)
admin.site.register(Level)

