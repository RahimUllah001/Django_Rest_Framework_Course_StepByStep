from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student

from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination,CursorPagination,LimitOffsetPagination
from .custompagination import customPage,customLimitOffset,customCursorPagination
# Create your views here.


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = PageNumberPagination
    # pagination_class = customPage #this is cutomize one paginatin in cutompagination.py file
    # pagination_class = customLimitOffset #this is cutomize one paginatin in cutompagination.py file
    pagination_class = customCursorPagination #this is cutomize one paginatin in cutompagination.py file