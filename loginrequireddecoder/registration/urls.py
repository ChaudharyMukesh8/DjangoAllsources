from django.urls import path
from registration import views
urlpatterns = [
     path('profile/',views.ProfiletemplateView.as_view(),name = 'profile')
]
