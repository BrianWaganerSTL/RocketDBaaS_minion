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

            myJson = '{"created_dttm":"%s","load_1min":%d,"load_5min":%d,"load_15min":%d}' % \
                     (str(timezone.now().replace(microsecond=0)), a[0], a[1], a[2])
            return HttpResponse(myJson)
        else:
            # Make up values since Windows can't get them
            myJson = '{"created_dttm":"%s","load_1min":%d,"load_5min":%d,"load_15min":%d}' % \
                     ((str(timezone.now().replace(microsecond=0))), randint(13, 30), randint(9, 15), randint(3, 7))
            return HttpResponse(myJson)
