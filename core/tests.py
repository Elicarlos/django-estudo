import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Cursos
from django.urls import reverse

class CursosModelTestes(TestCase):
    def teste_de_publicacao_futura_como_recente(self):
        time =timezone.now() + datetime.timedelta(days=30)
        cursos_futuros = Cursos(criado_em=time)
        self.assertIs(cursos_futuros.adcionado_recente(), False)


def adciona_curso(descricao, dias):
    time = timezone.now() + datetime.timedelta(days=dias)
    return Cursos.objects.create(descricao=descricao, criado_em=time)

class CursosIndexViewTest(TestCase):
    def test_no_curso(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nao ha cursos")
        self.assertQuerysetEqual(response.context['ultimos_cursos'], [])


