from random import randint
from sys import platform
import os

from django.http import HttpResponse
from django.utils import timezone


def LoadList(request):
    if request.method == 'GET':
        myJson = []
        if platform == "linux" or platform == "linux2":
            a = os.getloadavg()
            print(a)

            myJson = '{"created_dttm":"%s","load1min":%d,"load5min":%d,"load15min":%d}' % \
                     (str(timezone.now().replace(microsecond=0)), a)
            return HttpResponse(myJson)
        else:
            # Make up values since Windows can't get them
            myJson = '{"created_dttm":"%s","load_1min":%d,"load_5min":%d,"load_15min":%d}' % \
                     ((str(timezone.now().replace(microsecond=0))), randint(0, 30), randint(0, 15), randint(0, 9))
            return HttpResponse(myJson)
