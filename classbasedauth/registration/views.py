from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ProfiletemplateView(TemplateView):
    template_name = 'registration/profile.html'

    