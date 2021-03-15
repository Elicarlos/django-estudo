from django.contrib import admin
from .models import Cursos


class CursoAdmin(admin.ModelAdmin):
    # fields = ['descricao', 'preco', 'criado_em']

    list_display = ('descricao', 'preco', 'criado_em','adcionado_recente')
    list_filter = ['criado_em']
    search_fields = ['descricao']
    fieldsets = [
        (None, {'fields': ['descricao', 'preco']}),
        ('Informaçoes de datas', {'fields': ['criado_em']}),
    ]

# Register your models here.
admin.site.register(Cursos, CursoAdmin)
