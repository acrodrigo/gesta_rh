from django.urls import path, include
from . import views


urlpatterns = [
    path('list', views.HoraExtraList.as_view(), name="list_hora_extra"),
]
