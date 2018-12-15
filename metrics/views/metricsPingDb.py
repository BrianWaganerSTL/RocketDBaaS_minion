import psycopg2
from django.http import HttpResponse
from django.utils import timezone
from RocketDBaaS_minion.settings import MINION_DB, MINION_USER, MINION_PWD, MINION_PORT

def PingDbList(request):
    if request.method == 'GET':
       dbms_type = request.GET.get('dbms')
       # passwd = request.GET.get('passwd')

       if (dbms_type == 'PostgreSQL'):
           ping_db_status = 'Normal'
           startTs = timezone.now()
           try:
               conn = psycopg2.connect(dbname=MINION_DB, user=MINION_USER, password=MINION_PWD, host="localhost", port=MINION_PORT)
               conn.close()
           except psycopg2.Error as e:
               print("Unable to connect!")
               print(e.pgerror)
               print(e.diag.message_primary)
               print(e.diag.message_detail)
               ping_db_status = 'Critical'
           stopTs = timezone.now()
           myJson = '{"created_dttm":"%s","ping_db_status":"%s","ping_db_response_ms":%d}' % \
                     (str(timezone.now().replace(microsecond=0)), \
                      ping_db_status, \
                      int((stopTs - startTs).total_seconds() * 1000))
           return HttpResponse(myJson)

       elif (dbms_type == 'MongoDB'):
           ping_db_status = 'Normal'
           startTs = timezone.now()
           try:
               conn = psycopg2.connect(dbname=MINION_DB, user=MINION_USER, password=MINION_PWD, host="localhost", port=MINION_PORT)
               conn.close()
           except:
               ping_db_status = 'Blackout'
           stopTs = timezone.now()
           myJson = '{"created_dttm":"%s","ping_db_status":"%s","ping_db_response_ms":%d}' % \
                    (str(timezone.now().replace(microsecond=0)), \
                     ping_db_status, \
                     int((stopTs - startTs).total_seconds() * 1000))
           return HttpResponse(myJson)
