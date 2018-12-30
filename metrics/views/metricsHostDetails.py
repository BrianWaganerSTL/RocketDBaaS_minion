import datetime
from sys import platform
import psutil

# ipAddress
# cpuCount
# ramGb
# dataDbGb
# osVersion
# dbVersion
# lastServerRestart
# lastDbRestart
from django.http import HttpResponse


def HostDetailsList(request):
    if request.method == 'GET':
        cpuCount = psutil.cpu_count()

        lastReboot = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

        ramGb = round(psutil.virtual_memory().total / 1024 /1024 / 1024)

        if platform == "linux" or platform == "linux2":
            osVersion = "Linux"
        elif platform == "darwin":
            osVersion = "iOS"
        elif platform == "win32":
            osVersion = "Windows"

        dbVersion = "?"
        # if (osVersion == "Linux"):
        #     try:
        #         pwd.getpwnam('postgres')
        #         dbVersion = 'PostgeSQL'
        #     except KeyError:
        #         try:
        #             pwd.getpwnam('mongod')
        #             dbVersion = 'MongoDB'
        #         except KeyError:
        #             dbVersion = "?"

        myJson = '[{"cpuCount":%d,"lastReboot":"%s","ramGb":%d,"osVersion":"%s","dbVersion":"%s"}]' % (cpuCount, lastReboot, ramGb, osVersion, dbVersion)
        print('myJson=' + myJson)
        return HttpResponse(myJson)
