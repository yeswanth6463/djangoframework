from rest_framework import serializers
from foodapp.models import Fooditem,Category,Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'