from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Emergency
from .serializers import EmergencySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@api_view(['POST'])
def report_emergency(request):
    serializer = EmergencySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Emergency reported successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request,'index.html')


# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    return redirect('login')

@api_view(['POST'])
def report_emergency(request):
    if not request.user.is_authenticated:
        return Response({'error': 'Authentication required'}, status=401)

    serializer = EmergencySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Emergency reported successfully'}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def report_emergency(request):
    serializer = EmergencySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Emergency reported successfully'}, status=201)
    return Response(serializer.errors, status=400)