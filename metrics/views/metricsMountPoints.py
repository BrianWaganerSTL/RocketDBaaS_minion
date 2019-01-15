import re

import psutil

from django.http import HttpResponse
from django.utils import timezone


def MountPointsList(request):
    if request.method == 'GET':
        partitions = psutil.disk_partitions()
        myJson = '['
        count = 0
        for p in partitions:
            print(p.fstype + ',' + p.mountpoint)
            if (p.fstype):
                count += 1
                if (count > 1):
                    myJson += ','

                mntpoint = psutil.disk_usage(p.mountpoint)
                myJson += '{"created_dttm":"%s","mount_point":"%s","allocated_gb":%d,"used_gb":%d,"used_pct":%d}' % \
                         (str(timezone.now().replace(microsecond=0)), \
                          str(p.mountpoint).replace(':\\',''), \
                          mntpoint.total / 1024 / 1024 / 1024, \
                          mntpoint.used / 1024 / 1024 / 1024, \
                          mntpoint.percent)
        myJson += ']'
        return HttpResponse(myJson)
