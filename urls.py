from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^records/$', views.snow_plow_records, name='snow_plow_records'),
    url(r'^records$', views.snow_plow_records, name='snow_plow_records'),
]
