from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from .models import Student
from django import forms
from .forms import StudentForm
# Create your views here.

# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['name','email','password']
#     success_url = '/thanks/'

#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
#         form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'pass'})
#         return form

# class StudentUpdateView(UpdateView):
#     model = Student
#     fields = ['name','email','password']
#     success_url = '/thanks/'

#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
#         form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'pass'})
#         return form

class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks/'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanksupdate/'
    
    
class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class ThanksUpdateTemplateView(TemplateView):
    template_name = 'school/thanksupdate.html'