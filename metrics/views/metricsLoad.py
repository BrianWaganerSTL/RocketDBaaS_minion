from sys import platform

from django.http import HttpResponse


def LoadList(request):
    if request.method == 'GET':
       if platform == "linux" or platform == "linux2":
           import os

           a = os.getloadavg()
           print(a)
           print(os.getloadavg())

           return HttpResponse(a)
       else:
           return HttpResponse('')


