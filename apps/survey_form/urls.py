from django.conf.urls import url
from . import views          

urlpatterns = [
  url(r'^$', views.index),
  url(r'^send/process$', views.survey),
  url(r'^send$',views.output)

  ]