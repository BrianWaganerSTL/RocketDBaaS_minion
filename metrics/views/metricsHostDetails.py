import psycopg2
from sys import platform
import psutil

from django.http import HttpResponse
from django.utils import timezone
from RocketDBaaS_minion.settings import MINION_DB, MINION_DB_USER, MINION_DB_PWD, MINION_DB_PORT


def HostDetailsList(request):
    if request.method == 'GET':
        if platform == "linux" or platform == "linux2":
            osVersion = "Linux"
        elif platform == "darwin":
            osVersion = "Mac"
        elif platform == "win32":
            osVersion = "Windows"

        # ========================================================================
        if osVersion == "Windows":
            import socket
            ipAddress = socket.gethostbyname(socket.gethostname())
        elif osVersion == "Linux":
            import subprocess
            ipAddress = subprocess.run(["hostname","--ip-address"], universal_newlines=True, stdout=subprocess.PIPE).stdout[:-1];
        else:
            ipAddress=""

        # ========================================================================
        cpuCount = psutil.cpu_count()

        # ========================================================================
        lastReboot = timezone.datetime.fromtimestamp(psutil.boot_time()).astimezone()

        # ========================================================================
        ramGb = round(psutil.virtual_memory().total / 1024 /1024 / 1024)

        # ========================================================================
        try:
            dbGb = round(psutil.disk_usage('/opt/pgsql/data').total / 1024 /1024 / 1024)
            dbms_type = 'PostgreSQL'
        except:
            dbGb = round(psutil.disk_usage('/opt/mongodb/data').total / 1024 /1024 / 1024)
            dbms_type = 'MongoDB'

        # ========================================================================
        if (dbms_type == 'PostgreSQL'):
            try:
                conn = psycopg2.connect(dbname=MINION_DB, user=MINION_DB_USER, password=MINION_DB_PWD, host="localhost", port=MINION_DB_PORT)
            except psycopg2.Error as e:
                print("Unable to connect!")
                print(e.pgerror)
                print(e.diag.message_primary)
                print(e.diag.message_detail)

            cur = conn.cursor()
            try:
                cur.execute("select current_setting('server_version'), current_setting('server_version_num')")
            except:
                print("Can't select the DB versions")

            rows = cur.fetchall()
            for row in rows:
                print('   '+ row[1][1] + ', ' + row[2][1])
                dbVersion = row[1][1]
                dbVersionNumber = row[2][1]
            conn.close()

        # ========================================================================
        myJson = '{"created_dttm":"%s","cpuCount":%d,"ipAddress":"%s","lastReboot":"%s","ramGb":%d,"dbGb":%d,"osVersion":"%s","dbVersion":"%s","dbVersionNumber":%d}'\
                 % (str(timezone.now().replace(microsecond=0)), cpuCount, ipAddress, lastReboot, ramGb, dbGb, osVersion, dbVersion, dbVersionNumber)
        print('myJson=' + myJson)
        return HttpResponse(myJson)
