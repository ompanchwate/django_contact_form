from django.contrib import admin
from first.models import Contact # Import Contact function from models of first app
# Register your models here.
admin.site.register(Contact)  # Register the contact models