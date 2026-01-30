from django.contrib import admin
from .models import Grade, Subject


# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'value', 'date', 'comment')
    list_filter = ('student', 'subject', 'date')
    

