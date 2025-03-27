from django.shortcuts import render
from rest_framework.views import APIView
from foodapp.models import Recipe
from foodapp.serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework import generics

from rest_framework import mixins
from rest_framework.mixins import CreateModelMixin

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
    
# class FoodRecipeListView(generics.ListAPIView):
#     permission_classes=[]
#     authentication_classes=[]
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer

# class FoodRecipeRetriveView(generics.RetrieveAPIView):
        
#     permission_classes=[]
#     authentication_classes=[]
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#     lookup_field='id'
    
# class FoodRecipeCreateveView(generics.CreateAPIView):
#     permission_classes=[]
#     authentication_classes=[]
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
    

# class FoodRecipeUpdateView(generics.UpdateAPIView):
#     permission_classes=[]
#     authentication_classes=[]
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#     lookup_field='id'
    
# class FoodRecipeDeleteView(generics.DestroyAPIView):
#     permission_classes=[]
#     authentication_classes=[]
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#     lookup_field='id'


class foodRecipeListCreateView(generics.ListAPIView,mixins.CreateModelMixin):
    permission_classes=[]
    authentication_classes=[]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    
class foodRecipeUpdateDeleteRetriveView(generics.RetrieveAPIView,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    permission_classes=[]
    authentication_classes=[]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field='id'
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
    