from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.order_by("data_publicacao").filter(publicado=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_publicacao").filter(publicado=True)

    if "buscar" in request.GET:
        nome_pesquisado = request.GET['buscar']
        if nome_pesquisado:
            fotografias = fotografias.filter(nome__icontains=nome_pesquisado)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})