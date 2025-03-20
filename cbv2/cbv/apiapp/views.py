from django.shortcuts import render
import requests
from django.http import JsonResponse
from .models import TrainDetails
from .serializers import TrainDetailsSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

def userapi(request):
    response =requests.get('https://jsonplaceholder.typicode.com/users')
    user =response.json()
    # print(user)
    return render(request,'userapi.html',{'user':user})

def countryapi(request):
    response = requests.get('https://restcountries.com/v3.1/all')
    country = response.json()

    return render(request,'countryapi.html',{'country':country})

@csrf_exempt
def Trainapidata(request,id=0):
    if request.method =='GET':
        trains=TrainDetails.objects.all()
        trainserializer=TrainDetailsSerializer(trains,many=True)
        return JsonResponse(trainserializer.data,safe=False)  
    elif request.method=='POST':
        traindata=JSONParser().parse(request)
        trainserializer=TrainDetailsSerializer(data=traindata)
        if trainserializer.is_valid():
            trainserializer.save()
            return JsonResponse("Added Successfully",safe=False) 
    elif request.method=='PUT':
        traindata=JSONParser().parse(request)
        old_train_data=TrainDetails.objects.get(id=traindata['id'])
        trainserializer=TrainDetailsSerializer(old_train_data,data=traindata)
        if trainserializer.is_valid():
            trainserializer.save()
            return JsonResponse("Updated Successfully",safe=False)  
    elif request.method=='DELETE':
        traindata=TrainDetails.objects.get(id=id)
        traindata.delete()
        return JsonResponse("Deleted Successfully",safe=False)  
@csrf_exempt
def saveFile(request):
    files=request.FILES['file']
    file_name=default_storage.save(files.name,files)
    return JsonResponse(file_name,safe=False)                    


    



