from django.urls import path, include
from . import views


urlpatterns = [
    path('list', views.HoraExtraList.as_view(), name="list_hora_extra"),
    path('editar/<int:pk>', views.HoraExtraEdit.as_view() ,name="update_hora_extra")
]
