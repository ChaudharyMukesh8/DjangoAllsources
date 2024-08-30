from django.shortcuts import render
from .models import Student
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django import forms

from .forms import StudentForm
# Create your views here.


# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['name','email','password']
#     # success_url = '/thanks/'

#     # for adding the class on the text fields
#     def get_form(self):
#        form = super().get_form()
#        form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
#        form.fields['email'].widget = forms.EmailInput(attrs = {'class':'myclass'})
#        form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'myclass'})
#        return form

class ThanksTemplateView(TemplateView):
        template_name = 'school/thanks.html'

# class StudentDetailView(DetailView):
#         model = Student

class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks/'

       