from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Classroom)
admin.site.register(PreCourse)
admin.site.register(SelectCourse)
admin.site.register(School)
admin.site.register(Major)
admin.site.register(UserExtension)