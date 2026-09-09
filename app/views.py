from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Projeto


def lista_projetos(request):
    projetos = Projeto.objects.all()

    return render(
        request,
        'projetos/lista.html',
        {'projetos': projetos}
    )


def detalhe_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)

    return render(
        request,
        'projetos/detalhe.html',
        {'projeto': projeto}
    )



