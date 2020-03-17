from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


def sendEmail(request):
    return HttpResponse('sendEmail')