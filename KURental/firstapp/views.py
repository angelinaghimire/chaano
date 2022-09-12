from django.shortcuts import render
#from django.template import loader

# Create your views here.
from django.http import HttpResponse
from firstapp.models import RentDetails
from firstapp.models import RenterInfo


def index(request):
    return HttpResponse("index page")

def homepage(request):
    return HttpResponse("welcome to homepage")
def signin(request):
    return HttpResponse("welcome to sign in page")
def login(request):
    return HttpResponse("welcome to login page")
def dashboard(request):
    return HttpResponse("welcome to ku rental dashboard")
def output_page(request):
    return HttpResponse("welcome to outputpage")
def rentee_page(request):
    return HttpResponse("this is rentee dashboard")
def logout(request):
    return  HttpResponse("thanks for using our web page.")


