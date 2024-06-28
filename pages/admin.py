from django.contrib import admin

from .models import ContactUs, OurTeam

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'category']

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll']