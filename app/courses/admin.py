from django.contrib import admin

from django.contrib import admin
from .models.courses import Course
from .models.student import Student
from .models.language import Language
from .models.level import Level
from .models.teacher import Teacher


admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Language)
admin.site.register(Level)
admin.site.register(Teacher)

