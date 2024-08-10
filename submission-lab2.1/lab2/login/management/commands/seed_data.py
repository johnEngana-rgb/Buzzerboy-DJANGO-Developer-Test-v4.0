from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from login.models import Company, UserProfile


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Create a company
        company = Company.objects.create(name="HelloWorld Company", address="123 Main St, Cityville, Countryland")

        # Create users
        user1 = User.objects.create_user(username='john_doe', email='john.doe@example.com', password='P@$$w0rd')
        user2 = User.objects.create_user(username='jane_doe', email='jane.doe@example.com', password='P@$$w0rd')

        # Create profiles for user1
        UserProfile.objects.create(
            user=user1,
            company=company,
            phone_number="123-456-7890",
            bio="John's bio in English.",
            language="en",
            job_title="Software Developer"
        )
        UserProfile.objects.create(
            user=user1,
            company=company,
            phone_number="123-456-7890",
            bio="Biographie de John en français.",
            language="fr",
            job_title="Développeur de logiciels"
        )

        # Create profiles for user2
        UserProfile.objects.create(
            user=user2,
            company=company,
            phone_number="987-654-3210",
            bio="Jane's bio in English.",
            language="en",
            job_title="Project Manager"
        )
        UserProfile.objects.create(
            user=user2,
            company=company,
            phone_number="987-654-3210",
            bio="Biographie de Jane en français.",
            language="fr",
            job_title="Chef de projet"
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with users and profiles.'))
