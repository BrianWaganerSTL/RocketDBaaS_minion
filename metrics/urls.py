from django.urls import path

from metrics.views import metricsCpu, metricsMountPoints, metricsLoad, metricsDbTest

urlpatterns = [
    path('metrics/cpu', metricsCpu.CpuList),
    path('metrics/dbTest', metricsDbTest.DbTestList),
    path('metrics/load', metricsLoad.LoadList),
    path('metrics/mountPoints', metricsMountPoints.MountPointsList),
]
