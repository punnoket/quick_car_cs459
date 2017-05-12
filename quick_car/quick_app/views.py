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
GLOBAL_MECHANIC_OBJECT = None
GLOBAL_MECHANIC_LOGIN = None
GLOBAL_USER_LOGIN = None
GLOBAL_USER_JSON = None
GLOBAL_MECHANIC_JSON = None
GLOBAL_JOB = None
GOLBAL_DETAIL_FROM_USER = None
is_match = None
single_history = None
place_user = None

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

def map(request):
    return render(request, 'map.html')
def mecedit(request):
    return render(request, 'mecedit.html')

def sh2(request):
    return render(request, 'sh2.html')

def minihistory(request):
    return render(request,'minihistory.html')

def brows(request):
    return render(request, 'brows.html')

def editprofile(request):
    return render(request, 'editprofile.html')

def formbill(request):
    return render(request, 'formbill.html')

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

def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
	return render(request,'login.html')

def signup(request):
	return render(request,'signup.html')

def history(request):
	return render(request,'history.html')

def single_history(request):
	return render(request,'single_history.html')

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

def sing_up_new_user(request):
    json_data = json.loads(request.body)
    new_user = User.objects.create()
    new_user.username = json_data["username"]
    new_user.email = json_data["email"]
    new_user.password = json_data["password"]
    new_user.phone = json_data["phone"]
    new_user.locations = "14.065574699999999,100.6057261"
    new_user.save()
    new_user = serializers.serialize('json', notification)
    return HttpResponse(new_user, content_type='application/json')


@csrf_exempt
def show_notification(request):
	return render(request,'show_notification.html')

@csrf_exempt
def send_notification(request):
    global GLOBAL_USER_JSON
    global GLOBAL_MECHANIC_JSON
    global GOLBAL_DETAIL_FROM_USER
    json_data = json.loads(request.body)
    print(json_data)
    notification = Notification.objects.create()
    notification.garage_name = GLOBAL_MECHANIC_JSON["username"]
    notification.mechanic_name = "somchai"
    notification.client_name = GLOBAL_USER_JSON["user"]
    notification.license_plae_number = "15489-9859-98"
    notification.telephone = "098-2586547"
    notification.detail = GOLBAL_DETAIL_FROM_USER
    notification.to_user = GLOBAL_USER_JSON["user"]
    notification.is_read = 'false'
    notification.time = json_data['time']
    notification.date = json_data['date']
    notification.list_detail = json_data['detail']
    notification.save()
    user = {'user': "null", 'type': 'null'}
    user_json = json.dumps(user)
    return HttpResponse(user_json, content_type='application/json')


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
    global GLOBAL_MECHANIC
    json_data = json.loads(request.body)
    print(json_data)
    job = Job.objects.create()
    job.topics = json_data["detail"]
    job.date = json_data["date"]
    job.time = json_data["time"]
    job.locations = json_data["user_data"]["locations"]
    job.detail = json_data["detail"]
    job.mechanic = GLOBAL_MECHANIC
    job.user = json_data["user_data"]["user"]
    job.place = place_user
    job.price ="500"
    print(job.topics)
    job.save()
    user = {'user': "null", 'type': 'null'}
    user_json = json.dumps(user)
    return HttpResponse(user_json, content_type='application/json')

@csrf_exempt
def get_history(request):
    global GLOBAL_USER_JSON
    jobs = Job.objects.filter(user=GLOBAL_USER_JSON["user"])
    jobs_json = serializers.serialize('json', jobs)
    return HttpResponse(jobs_json, content_type='application/json')

@csrf_exempt
def auth_login(request):
    global GLOBAL_USER_LOGIN
    global GLOBAL_MECHANIC_LOGIN
    global GLOBAL_USER_JSON
    global GLOBAL_MECHANIC_JSON
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
                user = {'user': i.username, 'email': i.email, 'phone': i.phone, 'locations': i.locations}
                GLOBAL_USER_LOGIN = json.dumps(user)
                GLOBAL_USER_JSON = json.loads(GLOBAL_USER_LOGIN)
                check = 1


    mechanic_all = Mechanic.objects.all()
    for i in mechanic_all:
        if(username == i.username):
            if(password == i.password):
                request.session['username_mechanic'] = i.owner_name
                request.session['location_mechanic'] = i.locations
                #request.session['mechanic_object'] = i

                username_mechanic = {'username': i.owner_name, 'citizen_id': i.citizen_id, 'commercial_registration_no': i.commercial_registration_no, 'locations': i.locations, 'account': i.account}
                GLOBAL_MECHANIC_LOGIN = json.dumps(username_mechanic)
                GLOBAL_MECHANIC_JSON = json.loads(GLOBAL_MECHANIC_LOGIN)

                check = 2

    if(check == 1):
        user = {'user': GLOBAL_USER_JSON["user"], 'type': 'user'}
        user_json = json.dumps(user)
        print(user_json)
    elif(check == 2):
        user = {'user': GLOBAL_MECHANIC_JSON["username"], 'type': 'mechanic'}
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
def get_history_from_click(request):
    print(request)
    user = {'user': "null", 'type': 'null'}
    user_json = json.dumps(user)
    return HttpResponse(user_json, content_type='application/json')

@csrf_exempt
def click(request):
    global single_history
    print(request)
    json_data = json.loads(request.body)
    single_history = json_data["history"]
    user = {'user': "null", 'type': 'null'}
    user_json = json.dumps(user)
    return HttpResponse(user_json, content_type='application/json')

@csrf_exempt
def res_noti_to_bill(request):
    print(type(request.session['single_noti']))
    noti_json = json.dumps(request.session['single_noti'])
    return HttpResponse(noti_json, content_type='application/json')

@csrf_exempt
def res_history_to_single(request):
    global single_history
    single_history_json = json.dumps(single_history)
    print(single_history_json)
    return HttpResponse(single_history_json, content_type='application/json')

@csrf_exempt
def select_mechanic(request):
    global GLOBAL_MECHANIC
    global GLOBAL_MECHANIC_OBJECT
    global GOLBAL_DETAIL_FROM_USER
    global place_user
    json_data = json.loads(request.body)
    place_user = json.loads(request.body)["place"]
    print(place_user)
    GLOBAL_MECHANIC = json.loads(request.body)["mechanic"]
    GLOBAL_MECHANIC_OBJECT = json.loads(request.body)["mechanic_object"]
    GOLBAL_DETAIL_FROM_USER = json.loads(request.body)["detail"]
    user = {'user': "null", 'locations': 'null'}
    user_json = json.dumps(user)
    return HttpResponse(user_json, content_type='application/json')

@csrf_exempt
def is_match_complete(request):
    global is_match
    if(request.method == 'POST'):
        res = {'user': "null", 'type': 'null'}
        res_json = json.dumps(res)
        json_data = json.loads(request.body)
        is_match = json.loads(request.body)["answer"]
        print(is_match)

    elif(request.method == 'GET'):
        math = is_match
        res = {'user': "null", 'answer': math}
        res_json = json.dumps(res)
        print(is_match)
        is_match=""

    return HttpResponse(res_json, content_type='application/json')

@csrf_exempt
def get_user_match(request):
    global GLOBAL_MECHANIC
    global GLOBAL_USER_LOGIN
    global GLOBAL_USER_JSON

    print(GLOBAL_MECHANIC)
    json_data = json.loads(request.body)
    # print(request.session['username_location'])
    detail = "sdss"
    print(GLOBAL_USER_LOGIN)
    print('**********************')

    if(GLOBAL_MECHANIC == json_data["mechanic_name"]):
        user = {'user': GLOBAL_USER_JSON["user"], 'locations': "14.065574699999999,100.6057261", 'topic' : GOLBAL_DETAIL_FROM_USER, 'user_object': GLOBAL_USER_LOGIN}
    else:
        user = {'user': "null", 'locations': 'null','topic' : detail}

    user_json = json.dumps(user)
    return HttpResponse(user_json, content_type='application/json')
