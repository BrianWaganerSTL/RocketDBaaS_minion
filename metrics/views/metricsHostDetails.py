import psutil

# ipAddress
# cpuCount
# ramGb
# dataDbGb
# osVersion
# dbVersion
# lastServerRestart
# lastDbRestart

def CpuList(request):
    if request.method == 'GET':
        a = psutil.cpu_count()
        b = psutil.reboot()
