from django.shortcuts import render

# Create your views here.


def map(request):
    return render(request, 'map.html')

def login(request):
	return render(request,'login.html')