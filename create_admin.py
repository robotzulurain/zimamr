# create_admin.py
import os
import django
from django.contrib.auth import get_user_model

# adjust this if your project package name is not "amr_app"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amr_project.settings")
django.setup()

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if not password:
    print("DJANGO_SUPERUSER_PASSWORD not set — admin will not be created.")
else:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser '{username}' created.")
    else:
        print(f"Superuser '{username}' already exists.")
