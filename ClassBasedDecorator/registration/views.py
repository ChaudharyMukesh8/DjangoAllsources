from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

@method_decorator(login_required, name='dispatch')
class ProfiletemplateView(TemplateView):
    template_name = 'registration/profile.html'

# @method_decorator(login_required) 
# def dispatch(self,*args, **kwargs):
#     return super().dispatch(*args, **kwargs)


@method_decorator(staff_member_required,name = 'dispatch') 
class AbouttemplateView(TemplateView):
    template_name = 'registration/about.html'
    
# @method_decorator(staff_member_required) 
# def dispatch(self,*args, **kwargs):
#     return super().dispatch(*args, **kwargs)