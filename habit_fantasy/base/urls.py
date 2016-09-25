from django.conf.urls import url, include

from rest_framework import routers

from habit_fantasy.base import api, views


router = routers.DefaultRouter()
router.register(r'habit', api.HabitViewSet)
router.register(r'user', api.UserViewSet)


urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/', include(router.urls)),
]
