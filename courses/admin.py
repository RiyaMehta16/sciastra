# courses/admin.py
from django.contrib import admin
from .models import Course, Enrollment

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_date')
    search_fields = ('title',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment)
