from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView  
from .models import Student
# Create your views here.

class StudentListView(ListView):
    model = Student
    # template_name_suffix = '_get'
    # ordering =['roll']
    template_name = 'school/student.html'

    def get_queryset(self):
        return Student.objects.filter(course='Btech')

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context
    
    def get_template_names(self):
        if self.request.COOKIES['user'] == 'Mukesh':
         template_name = 'school/Mukesh.html'
        else:
         template_name = self.template_name
        return [template_name]
    
