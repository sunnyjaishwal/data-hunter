from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models.user import User
from .models.company_info import Company

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'user_type', 'is_staff', 'is_active', 'client_id')
    list_filter = ('user_type', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('user_type', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('client_id','email', 'password1', 'password2', 'user_type', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by', 'updated_by')  # optional: prevent changes via admin form

    def save_model(self, request, obj, form, change):
        if not change:  
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
