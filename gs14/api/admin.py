from django.contrib import admin
from .models import Student

@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']


    
    # 0d1f78928768857197e12d192b2e93511e2a4ac5	
    