
from django.shortcuts import render, get_object_or_404
from .models import Projeto


def lista_projetos(request):
    projetos = Projeto.objects.all()

    return render(
        request,
        'app/lista_projetos.html',
        {
            'projetos': projetos
        }
    )


def detalhe_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)

    return render(
        request,
        'app/detalhe_projeto.html',
        {
            'projeto': projeto
        }
    )
