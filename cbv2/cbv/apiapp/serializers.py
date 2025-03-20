from rest_framework import serializers
from apiapp.models import TrainDetails 


class TrainDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainDetails
        fields = '__all__'