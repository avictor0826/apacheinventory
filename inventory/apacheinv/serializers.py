from rest_framework import serializers
from .models import httpdinstance 
class httpdinstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = httpdinstance 
        fields = '__all__'
