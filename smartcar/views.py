from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .models import FeedbackData
from django.views.generic import TemplateView
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method == 'POST':
        print("heelo")
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("hiii")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            user = authenticate(username = username, password = raw_password)
            login(request,user)
            return redirect('home')

    else:
        form = SignUpForm()
    return render(request,'signup.html', {'form': form})


def feedback(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        print(user,name,email,mobile,message)
        feedback = FeedbackData()
        feedback.name=name
        feedback.email=email
        feedback.mobile=mobile
        feedback.message=message
        feedback.user=user
        feedback.save()
        data = {'message': 'Your valuable feedback is submitted. Thanks! '}
        return JsonResponse(data, safe=False)
    return render(request,"feedback.html")

