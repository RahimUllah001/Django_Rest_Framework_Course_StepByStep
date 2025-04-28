from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.

class StudentList(ListAPIView):
    # queryset = Student.objects.filter(passbywhome="fahim")
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city'] #this do exact match e.g 'where' condition in sql
    # filter_backends = [SearchFilter]
    filter_backends = [OrderingFilter]      #order by asc or desc
    # search_fields = ['name']  # Partial match this do partial match e.g 'like' conditin in sql 
    
    search_fields = ['^name']  # this is regex wheren name start with specific letter

#  we do the following when we want that only a creater can see his data like in blog post 
#     def get_queryset(self):
#         user = self.request.user  #request.user is always current user
#         return Student.objects.filter(passbywhome=user)