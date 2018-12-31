from sys import platform
import psutil

from django.http import HttpResponse
from django.utils import timezone


def HostDetailsList(request):
    if request.method == 'GET':
        if platform == "linux" or platform == "linux2":
            osVersion = "Linux"
        elif platform == "darwin":
            osVersion = "Mac"
        elif platform == "win32":
            osVersion = "Windows"

        if osVersion == "Windows":
            import socket
            ipAddress = socket.gethostbyname(socket.gethostname())
        elif osVersion == "Linux":
            import subprocess
            ipAddress = subprocess.run(["hostname","--ip-address"], universal_newlines=True, stdout=subprocess.PIPE).stdout[:-1];
        else:
            ipAddress=""

        cpuCount = psutil.cpu_count()

        lastReboot = timezone.datetime.fromtimestamp(psutil.boot_time()).astimezone()

        ramGb = round(psutil.virtual_memory().total / 1024 /1024 / 1024)

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

        myJson = '{"created_dttm":"%s","cpuCount":%d,"ipAddress":"%s","lastReboot":"%s","ramGb":%d,"osVersion":"%s","dbVersion":"%s"}'\
                 % (str(timezone.now().replace(microsecond=0)), cpuCount, ipAddress, lastReboot, ramGb, osVersion, dbVersion)
        print('myJson=' + myJson)
        return HttpResponse(myJson)
