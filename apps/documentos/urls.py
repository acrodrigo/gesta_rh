from django.urls import path, include
from . import views


urlpatterns = [
    path('novo/<int:funcionario_id>', views.DocumentoCreate.as_view(), name="create_documento"),
]
