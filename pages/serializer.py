from rest_framework import serializers

from .models import Services

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['title', 'description', 'image', 'title_info', 'number_info', 'text_info']