import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Cursos(models.Model):
    descricao = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=100 ,decimal_places=2)
    criado_em = models.DateTimeField('data_criacao')

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse('detalhes', args=[str(self.id)])
        

    def adcionado_recente(self):
        agora = timezone.now()
        return agora - datetime.timedelta(days=1) <= self.criado_em <= agora