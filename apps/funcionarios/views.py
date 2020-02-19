from django.http import HttpResponse
from .models import Funcionario
from django.views.generic import ListView

class FuncionarioList(ListView):
    model = Funcionario