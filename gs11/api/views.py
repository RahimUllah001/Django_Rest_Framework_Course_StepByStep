from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from django.shortcuts import render
from .custompermission import MyCustomPermission


class StudentModelviewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]      #this will show data to all means safe requeasts to all and post update create and delete to only authentocated
    # permission_classes = [DjangoModelPermissions]   #in this case data will show to authenticated users but other options will give it to go to admin side as superuser and will give this permission from backend
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]     #this is the combination of the above two
    permission_classes = [MyCustomPermission]       #these are my selfmade permison on specific object upto specific level means object level e.g the person whoc create the blog can do crud to it etc

      