from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# import requests
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from user_management.models import *
from user_management.views import *
from datetime import datetime
from django.contrib import messages



def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ipaddress = x_forwarded_for.split(',')[-1].strip()
    else:
        ipaddress = request.META.get('REMOTE_ADDR')
    return ipaddress

def signin_with_google(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        return render(request, 'user_management/signin_with_google.html')

@login_required
def after_signin_with_google(request):
    if request.user.is_authenticated:
        UserAuthLogs.objects.create(user_id=request.user.id, login_time=datetime.now(), ip_address=get_ip(request),session_key=request.session.session_key)
        return redirect('/dashboard')
    else:
        messages.error(request,'error')
        return HttpResponseRedirect('/')

def error_page(request):
    messages.error(request,'test error')
    return HttpResponseRedirect('/')