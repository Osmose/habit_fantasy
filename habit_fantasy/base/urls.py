from django.conf.urls import url

from habit_fantasy.base import views


urlpatterns = [
    url(r'^$', views.index),
]
