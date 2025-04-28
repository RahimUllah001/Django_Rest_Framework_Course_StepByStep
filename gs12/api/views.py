from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .models import Student
from .serializers import studentSerializer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['GET','POST', 'PUT','PATCH', 'DELETE']) # This decorator is used to define the type of request that the view function can accept. By default, it accepts GET requests.
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request , pk = None):
    # Get End Point
    if request.method == 'GET':
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = studentSerializer(student)
            return Response(serializer.data)
        student = Student.objects.all()
        serializer = studentSerializer(student, many=True)
        return Response(serializer.data)
    
    # Create End Point
    if request.method == 'POST':
        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created', 'data':serializer.data}, status=201)
        return Response(serializer.errors, status=400)
    
    # Update End Point Compltely
    if request.method == 'PUT':
    
        id = pk
        student = Student.objects.get(id=id)
        serializer = studentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors, status=400)
    

    # Partail Update End Point
    if request.method == 'PATCH':
    
        id = pk
        student = Student.objects.get(id=id)
        serializer = studentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors, status=400)

    #  Delete End Point
    if request.method == 'DELETE':
        id = pk
        student = Student.objects.get(id=id)
        student.delete()
        return Response({'msg':'Data Deleted'})
            
