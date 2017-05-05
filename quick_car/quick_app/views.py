from django.shortcuts import render ,redirect
from models import Notification, Mechanic, User, Job, NotificationSerializer
import json
from django.core import serializers
from django.http import JsonResponse
from rest_framework import viewsets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

username = ''

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

def map(request):
    return render(request, 'map.html')

def login(request):
	return render(request,'login.html')

def signup(request):
	return render(request,'signup.html')

def history(request):
	return render(request,'history.html')

def signgarage(request):
	return render(request,'signgarage.html')

def open_send_bill(request):
    return render(request,'send_notification.html')

def payment(request):
	return render(request,'payment.html')

def test(request):
	return render(request,'test.html')

@csrf_exempt
def show_notification(request):
	return render(request,'show_notification.html')

@csrf_exempt 
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
    notification = Notification.objects.filter(to_user=request.session['username'])
    notification_json = serializers.serialize('json', notification)
    print(notification_json)
    return HttpResponse(notification_json, content_type='application/json')

def send_job(request):
    return render(request,'create_job.html')

def create_job(request):
    #job = Job.objects.create()
    #job.save()
    json_data = json.loads(request.body)
    data = json_data['username']
    print(json_data)
    return redirect('login.html')

def auth_login(request):

    json_data = json.loads(request.body)
    username = json_data['username']
    password = json_data['password']
    check = 0

    user_all = User.objects.all()
    for i in user_all:
        if(username == i.username):
            if(password == i.password):
                request.session['username'] = i.username
                check = 1

    mechanic_all = Mechanic.objects.all()
    for i in mechanic_all:
        if(username == i.owner_name):
            if(password == i.password):
                request.session['username_machanic'] = i.username
                check = 2

    if(check == 1):
        user = {'user': request.session['username'], 'type': 'user'}
        user_json = json.dumps(user)
        print(user_json)
    elif(check == 2):
        user = {'user': request.session['username_machanic'], 'type': 'machanic'}
        user_json = json.dumps(user)
        print(user_json)
    else:
        user = {'user': "null", 'type': 'null'}
        user_json = json.dumps(user)

    return HttpResponse(user_json, content_type='application/json')
