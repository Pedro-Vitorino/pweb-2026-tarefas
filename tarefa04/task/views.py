from django.shortcuts import render
from .models import Tarefa
from datetime import date

def index(request):
    task = Tarefa.objects.all()
    context = {"tarefa": task}
    context['hoje'] = date.today()
    return render(request, 'task/index.html', context)
    
