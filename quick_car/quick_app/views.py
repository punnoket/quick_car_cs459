from django.shortcuts import render ,redirect
from models import Notification, Mechanic, User, Job
import json

# Create your views here.

username = ''

def map(request):
    return render(request, 'map.html')

def login(request):
	return render(request,'login.html')

def signup(request):
	return render(request,'signup.html')

def history(request):
	return render(request,'history.html')

def signupgarage(request):
	return render(request,'signupgarage.html')

def open_send_bill(request):
    return render(request,'send_notification.html')

def payment(request):
	return render(request,'payment.html')

def test(request):
	return render(request,'test.html')

def send_notification(request):
    print(request.GET.get('detail'))
    print(request.GET.get('user'))
    notification = Notification.objects.create()
    notification.topics = request.GET.get('detail')
    notification.detail = request.GET.get('detail')
    notification.to_user = request.GET.get('user')
    notification.is_read = 'false'
    notification.save()
    return redirect('login.html')

def get_notification(request):
    notification = Notification.objects.filter(to_user='pun')
    return render(request,'get_notification.html')

def send_job(request):
    return render(request,'create_job.html')

def create_job(request):
    #job = Job.objects.create()
    #job.save()
    json_data = json.loads(request.body)
    data = json_data['username']
    print(json_data)
    return redirect('login.html')
