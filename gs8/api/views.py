from django.shortcuts import render
from .models import Student
from .serializers import studentSerializer
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
# Create your views here.


# Here there are ingles class for each operation
# # Getting all data from the database
# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = studentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    

#     # Creating a new record in the database
# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = studentSerializer
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# # Getting a single record from the database
# class StudentRetrieve(GenericAPIView, RetrieveModelMixin):  
#     queryset = Student.objects.all()
#     serializer_class = studentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
# # Updating a single record in the database
# class StudentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = studentSerializer
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     # Deleting a single record from the database
# class StudentDelete(GenericAPIView, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = studentSerializer
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    


# To combine  the above endpoints upon which require pk and not
class StudentListCreate(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = studentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class StudentRetrieveUpdateDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = studentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)