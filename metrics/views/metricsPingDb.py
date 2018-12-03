import psycopg2
from django.http import HttpResponse
from django.utils import timezone


def PingDbList(request):
    if request.method == 'GET':
       dbms_type = request.GET.get('dbms')
       # passwd = request.GET.get('passwd')

       if (dbms_type == 'PostgreSQL'):
           ping_db_status = 'Normal'
           startTs = timezone.now()
           try:
               conn = psycopg2.connect("dbname='postgres' user='metrics_user' host='localhost' password='secure_password' connect_timeout=1")
               conn.close()
           except:
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
               conn = psycopg2.connect("dbname='postgres' user='metrics_user' host='localhost' password='secure_password' connect_timeout=1")
               conn.close()
           except:
               ping_db_status = 'Blackout'
           stopTs = timezone.now()
           myJson = '{"created_dttm":"%s","ping_db_status":"%s","ping_db_response_ms":%d}' % \
                    (str(timezone.now().replace(microsecond=0)), \
                     ping_db_status, \
                     int((stopTs - startTs).total_seconds() * 1000))
           return HttpResponse(myJson)
