from django.shortcuts import render ,redirect
from models import Notification, Mechanic, User, Job, NotificationSerializer
import json
from django.core import serializers
from django.http import JsonResponse
from rest_framework import viewsets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.

username = ''
GLOBAL_MECHANIC = None

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

def map(request):
    return render(request, 'map.html')
def contact(request):
    return render(request, 'contact.html')

def bill(request):
    return render(request, 'bill.html')

def mechanic_home(request):
    return render(request, 'mechanic_home.html')

def wait(request):
    return render(request, 'wait.html')

def match_complete(request):
    return render(request, 'match_complete.html')

def match_fail(request):
    return render(request, 'match_fail.html')

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

def sest(request):
    return render(request,'ttest.html')

@csrf_exempt
def show_notification(request):
	return render(request,'show_notification.html')

@csrf_exempt
def send_notification(request):
    json_data = json.loads(request.body)
    print(json_data)
    notification = Notification.objects.create()
    notification.topics = json_data['detail']
    notification.detail = json_data['detail']
    notification.to_user = request.session['username']
    notification.is_read = 'false'
    notification.time = json_data['time']
    notification.save()
    return redirect('login.html')

@csrf_exempt
def get_notification(request):
    notification = Notification.objects.filter(to_user=request.session['username'])
    notification_json = serializers.serialize('json', notification)
    #print(notification_json)
    return HttpResponse(notification_json, content_type='application/json')

@csrf_exempt
def send_job(request):
    return render(request,'create_job.html')


@csrf_exempt
def create_job(request):
    #job = Job.objects.create()
    #job.save()
    json_data = json.loads(request.body)
    data = json_data['username']
    #print(json_data)
    return redirect('login.html')


@csrf_exempt
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
                request.session['username_location'] = i.locations
                check = 1

    mechanic_all = Mechanic.objects.all()
    for i in mechanic_all:
        if(username == i.username):
            if(password == i.password):
                request.session['username_mechanic'] = i.owner_name
                request.session['location_mechanic'] = i.locations
                check = 2

    if(check == 1):
        user = {'user': request.session['username'], 'type': 'user'}
        user_json = json.dumps(user)
        print(user_json)
    elif(check == 2):
        user = {'user': request.session['username_mechanic'], 'type': 'mechanic'}
        user_json = json.dumps(user)
        print(user_json)
    else:
        user = {'user': "null", 'type': 'null'}
        user_json = json.dumps(user)

    return HttpResponse(user_json, content_type='application/json')

@csrf_exempt
def get_garage(request):
    garages = Mechanic.objects.all()
    garages_json = serializers.serialize('json', garages)
    #print(garages_json)
    return HttpResponse(garages_json, content_type='application/json')

@csrf_exempt
def get_location_garage(request):
    location_garage = {'username_mechanic': request.session['username_mechanic'], 'location': request.session['location_mechanic']}
    location_garage_json = json.dumps(location_garage)
    #print(location_garage_json)
    return HttpResponse(location_garage_json, content_type='application/json')

@csrf_exempt
def get_noti_from_click(request):
    json_data = json.loads(request.body)
    print(json_data["notification"])
    request.session['single_noti'] = json_data["notification"]
    user = {'user': "null", 'type': 'null'}
    user_json = json.dumps(user)
    return HttpResponse(user_json, content_type='application/json')

@csrf_exempt
def res_noti_to_bill(request):
    print(type(request.session['single_noti']))
    noti_json = json.dumps(request.session['single_noti'])
    return HttpResponse(noti_json, content_type='application/json')

@csrf_exempt
def select_mechanic(request):
    global GLOBAL_MECHANIC
    json_data = json.loads(request.body)
    GLOBAL_MECHANIC = json.loads(request.body)["mechanic"]
    request.session['match_mechanic'] = json_data
    print(request.session['match_mechanic'])
    noti_json = json.dumps(request.session['single_noti'])
    return HttpResponse(noti_json, content_type='application/json')

@csrf_exempt
def is_match_complete(request):
    user = {'user': "null", 'type': 'null'}
    user_json = json.dumps(user)
    return HttpResponse(user_json, content_type='application/json')

@csrf_exempt
def get_user_match(request):
    global GLOBAL_MECHANIC
    print(GLOBAL_MECHANIC)
    json_data = json.loads(request.body)
    # print(request.session['username_location'])
    detail = "sdss"

    if(GLOBAL_MECHANIC == json_data["mechanic_name"]):
        user = {'user': request.session['username'], 'locations': "14.065574699999999,100.6057261", 'topic' : detail}
    else:
        user = {'user': "null", 'locations': 'null','topic' : detail}

    user_json = json.dumps(user)
    return HttpResponse(user_json, content_type='application/json')
