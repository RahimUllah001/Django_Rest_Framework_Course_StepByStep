from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Student
from .serializers import studentSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.



class StudentAPI(APIView):
    # get all the data/Single data end point
    def get(self , request, pk=None, format=None):
        id = pk
        if id is not None:
            student = get_object_or_404(Student, id=id)
            serializer = studentSerializer(student)
            return Response(serializer.data)
        student = Student.objects.all()
        serializer = studentSerializer(student, many=True)
        return Response(serializer.data)
    
    
    # Create End Point
    def post(self,request,format=None):

        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created', 'data':serializer.data}, status=201)
        return Response(serializer.errors, status=400)
     
    # Update End Point Compltely
    def put(self , request, pk=None, format=None):
    
        id = pk
        student = Student.objects.get(id=id)
        serializer = studentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors, status=400)
    

    # Partail Update End Point
    def patch(self , request, pk=None, format=None):
    
        id = pk
        student = Student.objects.get(id=id)
        serializer = studentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors, status=400)

    #  Delete End Point
    def delete(self , request, pk=None, format=None):

        id = pk
        student = Student.objects.get(id=id)
        student.delete()
        return Response({'msg':'Data Deleted'})
            
