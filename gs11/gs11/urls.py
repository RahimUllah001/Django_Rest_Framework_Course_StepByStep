from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Router object
router = DefaultRouter()

# Register student viewset mean class with defalt router we are dioing this so that we habve not to maully accord url to every end point

# router.register('studentapi',views.StudentViewSet,basename='student')     #use this if want to use more code or use below for two lines

router.register('studentapi',views.StudentModelviewSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path("auth/",include('rest_framework.urls'))

]
