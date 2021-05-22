from django.shortcuts import redirect, render
from .models import TarefaDb
from .forms import ConteudoForm
# Create your views here.


def index(request):
    conteudo = TarefaDb.objects.all()
    form = ConteudoForm
    if request.method == 'POST':
        form = ConteudoForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('/')
    context = {
        'conteudos': conteudo,
        'form': form
    }
    return render(request, 'lista.html', context)

def delete_tarefa(request, id):
    deleteTarefa = TarefaDb.objects.get(id = id)
    deleteTarefa.delete()
    return redirect('/')