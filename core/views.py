from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# from django.template import loader
from .models import Cursos

# Create your views here.
# def index(request):
#     ultimos_cursos = Cursos.objects.order_by('-criado_em')#[:2]
#     # output = ', '.join([c.descricao for c in ultimos_cursos])
#     # template = loader.get_template('core/index.html')
#     context = {'ultimos_cursos': ultimos_cursos}
#     return render(request, 'core/index.html', context)


# # detalhes
# def detalhes(request, curso_id):
#     curso = get_object_or_404(Cursos, pk=curso_id)
#     return render(request, 'core/detalhes.html', {'curso': curso})


# def resultados(request, curso_id):
#     response = "Texte aqyu %s"
#     return HttpResponse(response, curso_id)


class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'ultimos_cursos'

    def get_queryset(self):
        return Cursos.objects.filter(
            criado_em__lte=timezone.now()
        ).order_by('criado_em')[:]



    
class DetalhesView(generic.DetailView):
    model = Cursos
    context_object_name = 'ultimos_cursos'

    template_name = 'core/detalhes.html'

