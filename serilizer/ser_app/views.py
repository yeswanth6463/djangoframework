from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import Tasskserializers
from .models import Task
# Create your views here.


@api_view(['GET'])
def serapp(request):
    api_urls={
        'list':'/task-list',
        'detail':'/task-detail/<str:pk>',
        'create':'/task-create',
        'update':'/task-update/<str:pk>',
        'delete':'/task-delete/<str:pk>',
    }
    
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    task = Task.objects.all()
    serializer =Tasskserializers(task, many=True) 
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    task = Task.objects.get(id=pk)
    serializer =Tasskserializers(task, many=False) 
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = Tasskserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
     
    return Response(serializer.data)

@api_view(['PUT'])
def taskUpdate(request,pk):
    task=Task.objects.get(id=pk)
    serializer = Tasskserializers(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
     
    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response("deleted")