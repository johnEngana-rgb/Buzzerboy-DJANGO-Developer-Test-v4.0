# admin.py

from django.contrib import admin
from .models import UserProfile, Company

def register_models():
    from .models import UserProfile, Company
    admin.site.register(UserProfile)
    admin.site.register(Company)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'job_title')  # Ensure these fields exist in the model
    search_fields = ('user__username', 'company__name', 'job_title')
    list_filter = ('company',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')  # Ensure these fields exist in the model
    search_fields = ('name',)
