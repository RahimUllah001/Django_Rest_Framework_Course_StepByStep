from django.shortcuts import render
import rest_framework
from .models import Student
from.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.

# single student data
def student_detail(request,pk):
    stu  = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)

    # print(stu)
    # print(serializer)
    # print(serializer.data)
    # print(json_data)

    # return HttpResponse(json_data,content_type = 'application/json')
    return JsonResponse(serializer.data)


# all student data

def student_detail_list(request):
    stu  = Student.objects.all()
    serializer = StudentSerializer(stu,many = True)
    # json_data = JSONRenderer().render(serializer.data)

    # print(stu)
    # print(serializer)
    # print(serializer.data)
    # print(json_data)

    # return HttpResponse(json_data,content_type = 'application/json')
    return JsonResponse(serializer.data,safe=False)
