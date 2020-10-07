from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import Students, Rooms, Teachers
from .serializers import StudentsSerializer, RoomsSerializer, TeachersSerializer

# Create your views here.

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all().order_by('name')
    serializer_class = StudentsSerializer

@csrf_exempt
def Students(request):
    
    if request.method == 'GET':
        stu = Students.objects.all()
        serializer = StudentsSerializer(Students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def Students(request, pk):

    try:
        stu = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentsSerializer(stu)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentsSerializer(stu, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        stu.delete()
        return HttpResponse(status=204)

################ Rooms ##############

class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all().order_by('numbers_of_rooms', 'numbers_of_students')
    serializer_class = RoomsSerializer

@csrf_exempt
def Rooms(request):
    
    if request.method == 'GET':
        rmm = Rooms.objects.all()
        serializer = StudentsSerializer(Rooms, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RoomsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def Rooms(request, pk):

    try:
        rmm = Rooms.objects.get(pk=pk)
    except Rooms.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentsSerializer(rmm)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RoomsSerializer(rmm, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        rmm.delete()
        return HttpResponse(status=204)

############## Teachers ################

class TeachersViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all().order_by('names_of_teachers')
    serializer_class = TeachersSerializer

@csrf_exempt
def Teachers(request):
    
    if request.method == 'GET':
        teach = Teachers.objects.all()
        serializer = TeachersSerializer(Teachers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TeachersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def Teachers(request, pk):

    try:
        teach = Teachers.objects.get(pk=pk)
    except Teachers.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TeachersSerializer(teach)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TeachersSerializer(teach, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        teach.delete()
        return HttpResponse(status=204)