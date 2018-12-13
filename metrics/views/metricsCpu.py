from sys import platform

import psutil
from django.utils import timezone

from django.http import HttpResponse


def CpuList(request):
    if request.method == 'GET':
        a = psutil.cpu_times_percent()

        if platform == "linux" or platform == "linux2":
            if len(a) == 8:
                cpuDetails = '"user":%d,"nice":%s,"system":%d,"idle":%d,"iowait":%d,"irq":%d,"softirq":"%d,"steal":%d}' % a
            elif len(a) == 9:
                cpuDetails = '"user":%d,"nice":%s,"system":%d,"idle":%d,"iowait":%d,"irq":%d,"softirq":"%d,"steal":%d,"guest":%d}' % a
            elif len(a) == 10:
                cpuDetails = '"user":%d,"nice":%s,"system":%d,"idle":%d,"iowait":%d,"irq":%d,"softirq":%d,"steal":%d,"guest":%d,"guest_nice":%d}' % a

        elif platform == "darwin":  # OS X
            cpuDetails = '"user":%d,"nice":%s,"system":%d,"idle":%d}' % a

        elif platform == "win32":
            cpuDetails = '"user":%d,"system":%d,"idle":%d,"interrupt":%d,"dpc":%d}' % a

        myJson = '{"created_dttm":"%s", %s' % (str(timezone.now().replace(microsecond=0)), cpuDetails)
        print('myJson=' + myJson)
        return HttpResponse(myJson)


