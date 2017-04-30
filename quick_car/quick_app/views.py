from django.shortcuts import render

# Create your views here.


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

def payment(request):
	return render(request,'payment.html')

def test(request):
	return render(request,'test.html')