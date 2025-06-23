from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Create default superuser on deploy"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@nomadic.com",
                password="ChangeThis123"
            )
            self.stdout.write(self.style.SUCCESS("Superuser created."))
        else:
            self.stdout.write("Superuser already exists.")
