from django.shortcuts import render, get_object_or_404, redirect
from .models import Bebe, Alimentacao, TrocaDeFralda, Sono, ConsultaMedica
from .forms import BebeForm, AlimentacaoForm, TrocaDeFraldaForm, SonoForm, ConsultaMedicaForm

def index(request):
    bebes = Bebe.objects.all()
    return render(request, 'bebes/index.html', {'bebes': bebes})

def detalhes_bebe(request, bebe_id):
    bebe = get_object_or_404(Bebe, pk=bebe_id)
    alimentacoes = Alimentacao.objects.filter(bebe=bebe)
    trocas = TrocaDeFralda.objects.filter(bebe=bebe)
    sonos = Sono.objects.filter(bebe=bebe)
    consultas = ConsultaMedica.objects.filter(bebe=bebe)
    return render(request, 'bebes/detalhes_bebe.html', {
        'bebe': bebe,
        'alimentacoes': alimentacoes,
        'trocas': trocas,
        'sonos': sonos,
        'consultas': consultas
    })

def adicionar_registro(request):
    if request.method == 'POST':
        form = BebeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BebeForm()
    return render(request, 'bebes/adicionar_registro.html', {'form': form})
