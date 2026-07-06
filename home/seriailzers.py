from rest_framework import serializers
from .models import Home


class HomeSeriailzer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields = '__all__'