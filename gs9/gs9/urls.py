
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # # The below is the endpoints for the combined operations
    # path('studentapi/',views.StudentList.as_view()),
    # path('studentapi/',views.StudentCreate.as_view()),
    # path('studentapi/',views.StudentRetrieve.as_view()),
    # path('studentapi/',views.StudentDestroy.as_view()),
    # path('studentapi/',views.StudentUpdate.as_view()),

    # this below two ccan do all crud 
    # path('studentapi/',views.StudentListCreate.as_view()),
    path('studentapi/<int:pk>/',views.StudentRetrieveUpdateDelete.as_view()),

    # To make this togather in two endpoints

]
