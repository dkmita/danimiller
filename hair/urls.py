from django.conf.urls import url

from . import views

app_name = 'hair'
urlpatterns = [
    url(r'^$', views.hair, name='index'),
]
