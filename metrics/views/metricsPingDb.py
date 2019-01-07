import psycopg2
from django.http import HttpResponse
from django.utils import timezone
from RocketDBaaS_minion.settings import MINION_DB, MINION_DB_USER, MINION_DB_PWD, MINION_DB_PORT

def PingDbList(request):
    if request.method == 'GET':
        dbms_type = request.GET.get('dbms')

        if (dbms_type == 'PostgreSQL'):
            ping_db_status = 'Normal'
            startTs = timezone.now()
            try:
                conn = psycopg2.connect(dbname=MINION_DB, user=MINION_DB_USER, password=MINION_DB_PWD, host="localhost", port=MINION_DB_PORT)
                conn.close()
            except psycopg2.Error as e:
                print("Unable to connect!")
                print(str(e))
                ping_db_status = 'Critical'
            stopTs = timezone.now()
            myJson = '{"created_dttm":"%s","ping_db_status":"%s","ping_db_response_ms":%d}' % \
                     (str(timezone.now().replace(microsecond=0)), \
                      ping_db_status, \
                      int((stopTs - startTs).total_seconds() * 1000))
            return HttpResponse(myJson)

        elif (dbms_type == 'MongoDB'):
            ping_db_status = 'UnKnown'
            startTs = timezone.now()
            # try:
            #     conn = psycopg2.connect(dbname=MINION_DB, user=MINION_DB_USER, port=MINION_DB_PORT)
            #     conn.close()
            # except
            #     ping_db_status = 'Blackout'
            stopTs = timezone.now()
            myJson = '{"created_dttm":"%s","ping_db_status":"%s","ping_db_response_ms":%d}' % \
                    (str(timezone.now().replace(microsecond=0)), ping_db_status, \
                     int((stopTs - startTs).total_seconds() * 1000))
            return HttpResponse(myJson)
