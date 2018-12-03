from time import gmtime

import psutil
from django.utils import timezone

from django.http import HttpResponse


def CpuList(request):
    if request.method == 'GET':
       a = psutil.cpu_times_percent()

       if len(a) == 5:  # Windows
           cpuDetails = '"user":"%d","system":"%d","idle":"%d","interrupt":"%d","dpc":"%d"}' % a
       elif len(a) == 6:
           cpuDetails = '"user":"%d","nice":"%s","system":"%d","idle":"%d","iowait":"%d","irq":"%d","softirq":"%d"}' % a
       elif len(a) == 7:
           cpuDetails = '"user":"%d","nice":"%s","system":"%d","idle":"%d","iowait":"%d","irq":"%d","softirq":"%d","steal":"%d"}' % a
       elif len(a) == 8:
           cpuDetails = '"user":"%d","nice":"%s","system":"%d","idle":"%d","iowait":"%d","irq":"%d","softirq":"%d","steal":"%d","guest":"%d"}' % a
       elif len(a) == 9:
           cpuDetails = '"user":"%d","nice":"%s","system":"%d","idle":"%d","iowait":"%d","irq":"%d","softirq":"%d","steal":"%d","guest":"%d","guest_nice":"%d"}' % a
       myJson = '{"created_dttm":"%s", %s' % (str(timezone.now().replace(microsecond=0)), cpuDetails)
       return HttpResponse(myJson)


