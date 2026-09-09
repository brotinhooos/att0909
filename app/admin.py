from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Categoria, Aluno, PerfilAcademico, Projeto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'matricula')


@admin.register(PerfilAcademico)
class PerfilAcademicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'link_lattes')


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'categoria', 'data_inicio')
    list_filter = ('categoria',)
    filter_horizontal = ('equipe',)
