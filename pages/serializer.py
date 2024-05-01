from rest_framework import serializers

from .models import Services, ContactUs

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['title', 'description', 'image', 'title_info', 'number_info', 'text_info']


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'category', 'description']