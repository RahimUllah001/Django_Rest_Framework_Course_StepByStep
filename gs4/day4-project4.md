
# Django CRUD API Using Class-Based Views

This project demonstrates how to create a CRUD API (Create, Read, Update, Delete) using Django's class-based views. The API enables basic operations on a `Student` model with fields `id`, `name`, `roll`, and `city`. This file explains the structure and flow of the implementation, as well as how each function operates within the API.

## Project Structure

The project has the following components:

1. `urls.py`: Defines the URL routing for the CRUD operations.
2. `views.py`: Contains class-based views handling CRUD operations.
3. `models.py`: Defines the `Student` model used for this API.
4. `serializers.py`: Defines the serializer for data validation and serialization.
5. `myapp.py`: Client-side code for testing CRUD operations.

### `models.py`
The `Student` model represents each student entity and includes the following fields:
```python
from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    city = models.CharField(max_length=70)
```

### `serializers.py`
The `StudentSerializer` handles data validation and serialization for the `Student` model.
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=70)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
```

### `views.py`
This file contains a class-based view `StudentApi` with methods for handling CRUD operations.

- **GET**: Retrieve all students or a single student by ID.
- **POST**: Create a new student record.
- **PUT**: Update an existing student record.
- **DELETE**: Delete a student record.

```python
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
import io

@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def get(self, request, *args, **kwargs):
        id = request.GET.get('id', None)
        if id:
            try:
                student = Student.objects.get(id=id)
                serializer = StudentSerializer(student)
                return JsonResponse(serializer.data, safe=False)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse({'msg': 'Data created'}, status=201)
        return HttpResponse(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse({'msg': 'Data updated'}, status=200)
        return HttpResponse(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        return JsonResponse({'msg': 'Data deleted'}, status=204)
```

### `urls.py`
The URL configuration routes requests to the `StudentApi` view.
```python
from django.urls import path
from .views import StudentApi

urlpatterns = [
    path('studentapi/', StudentApi.as_view()),
]
```

### Client-Side Testing (`myapp.py`)
To test the API, use the following functions for each CRUD operation.

```python
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    params = {'id': id} if id else {}
    r = requests.get(url=URL, params=params)
    print(r.json())

def post_data():
    data = {'name': 'New Student', 'roll': 105, 'city': 'New City'}
    r = requests.post(url=URL, data=json.dumps(data))
    print(r.json())

def update_data():
    data = {'id': 1, 'name': 'Updated Student', 'roll': 106, 'city': 'Updated City'}
    r = requests.put(url=URL, data=json.dumps(data))
    print(r.json())

def delete_data():
    data = {'id': 1}
    r = requests.delete(url=URL, data=json.dumps(data))
    print(r.json())
```

## Control Flow

1. **Request Receives**: When a request (GET, POST, PUT, DELETE) is sent to `studentapi/`, it is routed to the `StudentApi` view.
2. **Request Handling**:
   - **GET**: Checks if an `id` parameter is present. If yes, returns the student data with that ID; otherwise, it returns all students.
   - **POST**: Receives data to create a new student. Validates data using `StudentSerializer` and saves if valid.
   - **PUT**: Receives an `id` and updates the corresponding student with any provided fields.
   - **DELETE**: Receives an `id` and deletes the student with that ID.
3. **Response**: Each method responds with JSON data or status codes indicating the success or failure of the operation.

This control flow enables streamlined management of student data, with efficient routing and handling for each CRUD operation.
