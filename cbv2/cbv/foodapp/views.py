from django.shortcuts import render
from rest_framework.views import APIView
from foodapp.models import Recipe
from foodapp.serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
# class FoodRecipeListdetailsview(APIView):
#     def get(self,request):
#         data=Recipe.objects.all()
#         foodserializer =RecipeSerializer(data,many=True)
#         return Response(foodserializer.data)
    
#     def post(self,request):
#         data=Recipe.objects.all()
#         foodserializer =RecipeSerializer(data,many=True)
#         return Response(foodserializer.data)
    
class FoodRecipeListView(generics.ListAPIView):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
