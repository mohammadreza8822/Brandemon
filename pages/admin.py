from django.contrib import admin

from .models import ContactUs, OurTeam, Faq, Price

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'category']

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll']

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['title']
