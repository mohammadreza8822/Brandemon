from django.contrib import admin

from .models import Services

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    model = Services
    fields = ['icon','title','slug','description','image','title_info','number_info','text_info']
    prepopulated_fields = {"slug": ["title"]}
