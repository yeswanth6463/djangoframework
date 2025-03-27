from rest_framework import serializers
from .models import Task

class Tasskserializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'