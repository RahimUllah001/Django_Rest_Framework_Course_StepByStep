
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # the below is the endpoints for the single operation
    # path('studentapi/',views.StudentList.as_view()),
    # path('studentapi/',views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentRetrieve.as_view()),
    # path('studentapi/<int:pk>/',views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentDelete.as_view()),

    # The below is the endpoints for the combined operations
    path('studentapi/',views.StudentListCreate.as_view()),
    path('studentapi/<int:pk>/',views.StudentRetrieveUpdateDelete.as_view()),


    # To make this togather in two endpoints

]
