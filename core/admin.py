from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, Company, UserProfile

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User
    list_display = ('email','first_name','is_staff')
    ordering = ('email',)
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('email','password')}),
        ('Personal', {'fields': ('first_name','last_name')}),
        ('Permissions', {'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
    )
    add_fieldsets = ((None, {'classes':('wide',),'fields':('email','password1','password2')}),)

admin.site.register(Company)
admin.site.register(UserProfile)
