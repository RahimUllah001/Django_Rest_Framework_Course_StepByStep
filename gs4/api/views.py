from django.shortcuts import render
import requests
from .models import Student
import io
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
from django.views import View
# Create your class-based views here.

@method_decorator(csrf_exempt,name='dispatch') # Disable CSRF verification for simplicity; use with caution in production.
class StudentApi(View):
    def get(self,request,*args,**kwargs):
        # Get 'id' from query parameters
        id = request.GET.get('id', None)

        if id is not None:
            try:
                # Fetch single student by id
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return JsonResponse(serializer.data, safe=False)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)

        # Fetch all students if no id is provided
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data= pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')
        
        
    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data = pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data createrrrrrrrrrrrrrrrrrrrrrrrrrrrwazzzzzzzzzzzd'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')
        
            

    def delete(self,request,*args,**kwargs):
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id')
            stu = Student.objects.get(id=id)
            stu.delete()
            res = {'msg':'object deleted'}
            return JsonResponse(res, safe=False)
    

