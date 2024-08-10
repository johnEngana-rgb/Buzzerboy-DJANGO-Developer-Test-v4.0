from django.contrib import admin
from .models import UserProfile, Company

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'phone_number', 'language']  # Ensure these fields exist in the model
    search_fields = ['user__username', 'company__name']
    list_filter = ['company']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']  # Ensure these fields exist in the model
    search_fields = ['name']
