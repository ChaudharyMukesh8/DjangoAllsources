from typing import Any
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView,RedirectView
from django.views import View

# Create your views here.

# This function will add new items and show All Items.....

# This is class based view..
class UserAddShowView(TemplateView):
  template_name = 'enroll/addandshow.html'
  def get_context_data(self,*arg,**kwargs) :
    context = super().get_context_data(**kwargs)
    fm = StudentRegistration()
    stud =User.objects.all()
    context = {'stu':stud, 'form':fm}
    return context
  
  def post(self,request):
     fm = StudentRegistration(request.POST)
     if fm.is_valid():
        nm = fm.cleaned_data['name']
        em = fm.cleaned_data['email']
        ps = fm.cleaned_data['password']
        reg = User(name =nm, email=em, password=ps)
        fm.save()
        return HttpResponseRedirect('/')


# This function will Update by using Class based view...

class UserUpdateView(View):
  def get(self,request,id):
    pi = User.objects.get(pk = id)
    fm = StudentRegistration(request.POST,instance=pi)
    return render(request,'enroll/updatestudent.html', {'form':fm})
  
  def post(self,request,id):

    pi = User.objects.get(pk = id)
    fm = StudentRegistration(request.POST,instance=pi)
    if fm.is_valid():
     fm.save()
    return HttpResponseRedirect('/')

  

# This Function will Delete data by using class based view
class UserDeleteView(RedirectView):
  url = '/'
  def get_redirect_url(self, *args, **kwargs):
    del_id = kwargs['id']
    User.objects.get(pk=del_id).delete()
    return super().get_redirect_url(*args, **kwargs)
  


