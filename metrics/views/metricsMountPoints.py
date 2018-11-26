import psutil

from django.http import HttpResponse


def MountPointsList(request):
    if request.method == 'GET':
       a = psutil.cpu_times_percent()

       if len(a) == 5:  # Windows
           myJson = '{"user":"%d","system":"%d","idle":"%d","interrupt":"%d","dpc":"%d"}' % a
       elif len(a) == 6:
           myJson = '{"user":"%d","nice":"%s","system":"%d","idle":"%d","iowait":"%d","irq":"%d","softirq":"%d"}' % a
       elif len(a) == 7:
           myJson = '{"user":"%d","nice":"%s","system":"%d","idle":"%d","iowait":"%d","irq":"%d","softirq":"%d","steal":"%d"}' % a
       elif len(a) == 8:
           myJson = '{"user":"%d","nice":"%s","system":"%d","idle":"%d","iowait":"%d","irq":"%d","softirq":"%d","steal":"%d","guest":"%d"}' % a
       elif len(a) == 9:
           myJson = '{"user":"%d","nice":"%s","system":"%d","idle":"%d","iowait":"%d","irq":"%d","softirq":"%d","steal":"%d","guest":"%d","guest_nice":"%d"}' % a

       return HttpResponse(myJson)


