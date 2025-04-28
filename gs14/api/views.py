from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class StudentModelviewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    # How to generate token write this in cli and it will give two token one will be access token and second one will be refresh token acesstoken time 5 minute and refresh token time is one day .
    # rahim@rahim-Aspire-A315-55G:/media/rahim/RAHIM ASKAR/1aGeeky shows/DRF/gs14$ http POST http://127.0.0.1:8000/gettoken/ username="user1" password="Admin@a1"

    # when an access otken is expeired how we wil generate a new access token
    # we will write the bewlo command
    # rahim@rahim-Aspire-A315-55G:/media/rahim/RAHIM ASKAR/1aGeeky shows/DRF/gs14$ http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MjMzMzQzNiwiaWF0IjoxNzQyMjQ3MDM2LCJqdGkiOiI0Y2E5YjI1M2E5NWM0YmU4YWZlYTZmYjNlMzBjNzA2MiIsInVzZXJfaWQiOjJ9.8wc5yBbeCeZsscAYK6Xt6U1inAXhl8qA7AeudJ0ci0"

    # Get Request to show data then writ ethe bewlo comand in authorzation bearer i have actully written the access token
    # rahim@rahim-Aspire-A315-55G:/media/rahim/RAHIM ASKAR/1aGeeky shows/DRF/gs14$ http  http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMjQ3Njg0LCJpYXQiOjE3NDIyNDcwMzYsImp0aSI6ImU1NzdiMDFkMjJhODQ2Yjg5MTIwYTE3OWJiMDFiZWZmIiwidXNlcl9pZCI6Mn0.BJebQjJy8ZlBeNvA5PB-u67nq620eypPsMWYgHxXaHw'

    # How to insert data  use the access comenad in authorization bearer
    # http -f POST http://127.0.0.1:8000/studentapi/ name=abdurehman roll=66 city=charsada 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMjQ4MTY0LCJpYXQiOjE3NDIyNDcwMzYsImp0aSI6IjQ4MzM4MjZjMTFlZDQxMGZhYzUxNDJiYTNmNGFiZDViIiwidXNlcl9pZCI6Mn0.gjlpIPisfTcZh3DJG-VtS6s-aVxQMfeDO9ia6n0soKw'

    # How to update data
    # http -f PUT http://127.0.0.1:8000/studentapi/11/ name=abdurehman roll=66 city=chavvvvvvvvvrsada 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMjQ4Mzk1LCJpYXQiOjE3NDIyNDcwMzYsImp0aSI6IjVlYjAyNzQ4YTVlZjQwY2FiMjllOThmMmU5YTQxOTdkIiwidXNlcl9pZCI6Mn0.unMsFfwr2gCfCTaExreOI3Rjv2_-5iWx4JDLfOTVkco'
    # Delete data
    # http -f DELETE http://127.0.0.1:8000/studentapi/11/ name=abdurehman roll=66 city=chavvvvvvvvvrsada 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMjQ4Mzk1LCJpYXQiOjE3NDIyNDcwMzYsImp0aSI6IjVlYjAyNzQ4YTVlZjQwY2FiMjllOThmMmU5YTQxOTdkIiwidXNlcl9pZCI6Mn0.unMsFfwr2gCfCTaExreOI3Rjv2_-5iWx4JDLfOTVkco'


