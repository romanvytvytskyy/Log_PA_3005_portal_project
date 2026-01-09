from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ('Ролі та профіль', {'fields': ('is_moderator', 'is_student', 'avatar', 'bio')}),
    )
    
admin.site.register(User, CustomUserAdmin)