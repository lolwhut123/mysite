from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^matchups$', views.matchups, name='matchups'),
    url(r'^mechanics$', views.mechanics, name='mechanics'),
    url(r'^tricks$', views.tricks, name='tricks'),
    url(r'^job_in_teamfights$', views.job_in_teamfights, name='job_in_teamfights'),
]
