from django.urls import path

from metrics.views import metricsCpu, metricsMountPoints, metricsLoad, metricsPingDb, metricsHostDetails

urlpatterns = [
    path('metrics/cpu', metricsCpu.CpuList),
    path('metrics/pingdb', metricsPingDb.PingDbList),
    # path('metrics/pingserver', metricsPingDb.PingDbList),  # Not needed since it's just a ping
    path('metrics/load', metricsLoad.LoadList),
    path('metrics/mountpoints', metricsMountPoints.MountPointsList),
    path('metrics/hostdetails', metricsHostDetails.HostDetailsList),
]
