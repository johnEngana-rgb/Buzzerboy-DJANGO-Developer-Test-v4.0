# models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.conf import settings

LANGUAGES = settings.LANGUAGES
class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()  # Make sure this field exists

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    language = models.CharField(
        max_length=5,
        choices=LANGUAGES,
        default='en',
        verbose_name=_('Preferred Language')
    )
    job_title = models.CharField(max_length=255, null=True, blank=True)  # Add this line if you need 'job_title'

    def __str__(self):
        return f"{self.user.email} - {self.company.name}"
