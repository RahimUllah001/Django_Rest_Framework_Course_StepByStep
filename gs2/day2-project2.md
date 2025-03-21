# Django REST API with Python `requests` Library

This project demonstrates how to send data from a Python frontend using the `requests` library to a Django REST API for saving data in the database.

## Project Structure

- **Frontend: `myapp.py`**  
  A simple Python script that sends a POST request with student data to the Django backend.

- **Backend: Django REST API**  
  The Django backend consists of a model serializer (`StudentSerializer`) and a view (`student_create`) that handles incoming data and stores it in the database.

## Frontend (`myapp.py`)

In the `myapp.py` script, the `requests` library is used to send a POST request to the Django API.

```python
import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'rahim',
    'roll': 101,
    'city': 'bannu'
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
response_data = r.json()

print(response_data)
```

### Explanation:
- **URL:** The endpoint where the data will be posted.
- **Data:** A dictionary containing student information (`name`, `roll`, and `city`).
- **Request:** A POST request is made to send the JSON data to the Django API.
- **Response:** The response from the server is printed, containing either success or error messages.

## Backend (`serializer.py` and `views.py`)

### Serializer (`serializer.py`)
The `StudentSerializer` converts incoming JSON data into Python objects and validates them before saving to the database.

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=70)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
```

### View (`views.py`)
The `student_create` view receives POST requests, parses the data, validates it using the serializer, and saves it in the database.

```python
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentSerializer

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
```

### Key Concepts:
- **`@csrf_exempt`:** This decorator is used to bypass CSRF verification for the view.
- **`JSONParser`:** Used to parse the incoming JSON data.
- **`StudentSerializer`:** Validates and saves the data.
- **`JSONRenderer`:** Converts the response data into JSON format before sending it back to the frontend.

## Running the Project

1. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

2. Run the `myapp.py` script to send the data:
    ```bash
    python myapp.py
    ```

## Expected Output

If the data is valid, you will see the following response:

```json
{
    "msg": "Data created"
}
```

If the data is invalid, the response will contain error messages:

```json
{
    "name": ["This field is required."]
}
```

## Conclusion

This project demonstrates how to send data from a Python frontend to a Django backend using the `requests` library. The Django API receives the data, validates it using a serializer, and saves it in the database, returning a JSON response.



//////////////////////////////////////////////////////////////////////////////////////////////////
myapp.py or frontend i.e clientside
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    params = {}
    if id is not None:
        params = {'id': id}  # Use params for query parameters
    
    # Correctly use params instead of data for GET requests
    r = requests.get(url=URL, params=params)  # Pass params here
    data = r.json()
    print(data)

# get_data()  # Fetch the student with id 1


def post_data():
    data = {
        'name':'abd',
        'roll':104,
        'city':'Dhaband'
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data   = json_data)
    data = r.json()
    print(data)
# post_data()

def update_data():
    data = {
        'id':2 ,
        'name':'Muhammad  wazir',
        'roll':1104,
        'city':'bannu'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data  = json_data)
    data = r.json()
    print(data)
# update_data()

def delete_data():
    data = {
        'id':3 
    }

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data  = json_data)
    data = r.json()
    print(data)
# delete_data()

url.py
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentApi.as_view())
]

views.py:
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


    myapp.py or frontend i.e clientside
import requests

import json



URL = "http://127.0.0.1:8000/studentapi/"



def get_data(id=None):

    params = {}

    if id is not None:

        params = {'id': id}  # Use params for query parameters

    

    # Correctly use params instead of data for GET requests

    r = requests.get(url=URL, params=params)  # Pass params here

    data = r.json()

    print(data)



# get_data()  # Fetch the student with id 1





def post_data():

    data = {

        'name':'abd',

        'roll':104,

        'city':'Dhaband'

    }



    json_data = json.dumps(data)

    r = requests.post(url = URL, data   = json_data)

    data = r.json()

    print(data)

# post_data()



def update_data():

    data = {

        'id':2 ,

        'name':'Muhammad  wazir',

        'roll':1104,

        'city':'bannu'

    }



    json_data = json.dumps(data)

    r = requests.put(url = URL, data  = json_data)

    data = r.json()

    print(data)

# update_data()



def delete_data():

    data = {

        'id':3 

    }



    json_data = json.dumps(data)

    r = requests.delete(url = URL, data  = json_data)

    data = r.json()

    print(data)

# delete_data()

url.py
from django.contrib import admin

from django.urls import path

from api import views



urlpatterns = [

    path('admin/', admin.site.urls),

    path('studentapi/', views.StudentApi.as_view())

]

views.py:
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

serializers.py:
from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=70)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    def update(self,instance,validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance

model.py 
from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    city = models.CharField(max_length=70)

in this project I have demonstrated that how to make a crud API using classbased views plz make md file containing all the detail how achieve the things ad n provide me the link of the md file so that I can download in thelast section  md file should contain the control flow how it works 
    

*****plz provide me only link of the md file so that I can download*******88
