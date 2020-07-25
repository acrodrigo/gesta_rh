from django.urls import path, include
from . import views


urlpatterns = [
    path('list', views.HoraExtraList.as_view(), name="list_hora_extra"),
    path('editar/<int:pk>', views.HoraExtraEdit.as_view() ,name="update_hora_extra"),
    path('delete/<int:pk>', views.HoraExtraDelete.as_view() ,name="delete_hora_extra"),
    path('create', views.HoraExtraCreate.as_view(), name="create_hora_extra")

]
