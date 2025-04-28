from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

from django.shortcuts import render

# We will use this class or the below 2nd class

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)

        return Response(serializer.data)
    

    def retrieve(self, request,pk=None):
        id = pk 
        if id != None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
    def create(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"MSg":"successfully created"})
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


    def update(self,request,pk=None):
        id= pk
        if id != None:
            stu = Student.objects.get(id=id)

            serializer = StudentSerializer(stu,data = request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({"message":"data complete updated"})
            else:
                return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

        

    def partial_update(self,request,pk=None):
        id= pk
        if id != None:
            stu = Student.objects.get(id=id)

            serializer = StudentSerializer(stu,data = request.data,partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({"message":"data complete updated"})
            else:
                return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
            
    def destroy(self,reqeust,pk):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({"msg":"DAta deleted"})

        
# if i want to achieve from the above all in class and two line then i will use modelview set

class StudentModelviewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # i can do the belwo work globally for al classess i will achieve this in setting .py in the buttom
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
      


# Only for Read only
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # if i want to not implement global authentication
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [AllowAny]
    permission_classes = [IsAdminUser]
