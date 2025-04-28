from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

# custom throthling
from .custom_throttling import CustomThrotleRate


# fro sett throttle i have to write the below code in setting.py in last


# REST_FRAMEWORK = {
#     'DEFAULT_THROTTLE_RATES':{
#         'anon': '2/day',
#         'user': '5/hour'
#     }
# }
class StudentModelviewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle,UserRateThrottle] Global Rates
    throttle_classes = [AnonRateThrottle,CustomThrotleRate] #Customize  Rates






