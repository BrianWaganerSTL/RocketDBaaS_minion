import re

import psutil

from django.http import HttpResponse
from django.utils import timezone


def MountPointsList(request):
    if request.method == 'GET':
        partitions = psutil.disk_partitions()
        myJson = []
        count = 0
        for p in partitions:
            if (p.fstype):
                count += 1
                oneJson = '{"created_dttm":"%s","mount_point":"%s","allocated_gb":%d,"used_gb":%d,"used_pct":"%d"}' % \
                         (str(timezone.now().replace(microsecond=0)), \
                          re.sub(':\\\\','',p.mountpoint), \
                          psutil.disk_usage(p.mountpoint).total / 1024 / 1024 / 1024, \
                          psutil.disk_usage(p.mountpoint).used / 1024 / 1024 / 1024, \
                          psutil.disk_usage(p.mountpoint).percent)
                if (count > 1 ):
                    oneJson = oneJson + ','
                myJson.append(oneJson)

        return HttpResponse(myJson)

