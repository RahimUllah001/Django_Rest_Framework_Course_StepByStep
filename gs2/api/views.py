from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# single student data
@csrf_exempt        #if we ot ujse this it will give n error csrf token required by doing this we bypas csrf token
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data creted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
            # return JsonResponse(serializer.data)
        json_data = JSONRenderer().render(serializer.errors)            
        return HttpResponse(json_data,content_type = 'application/json')





    


