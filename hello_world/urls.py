from django.conf.urls import url

from . import views

app_name = 'hello_world'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
