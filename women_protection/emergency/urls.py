from django.urls import path
from .views import report_emergency,index, register, user_login, user_logout

urlpatterns = [
    path('',index, name = 'index'),
    path('report/', report_emergency, name='report_emergency'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
