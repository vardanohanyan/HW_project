from django.contrib import admin
from .models import Human

# Problem 3
#
# We want to see the Human model in the admin panel. Create a HumanAdmin class in admin.py
# We want to display human's name, surname and age (*note, Human class has no field age) on the admin panel.

admin.site.register(Human)