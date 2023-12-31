from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Local(models.Model):
    nome = models.CharField(max_length=240)
    rua = models.CharField(max_length=240)
    numero = models.IntegerField()

    def __str__(self):
        return f'{self.nome} na rua {self.rua}'

    class Meta:
        verbose_name_plural = "Locais"


class Convidado(models.Model):
    nome = models.CharField(max_length=240)
    email = models.EmailField(null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.email}'


class Compromisso(models.Model):
    descricao = models.CharField(max_length=240)
    data_inicio = models.DateTimeField(null=True)
    data_fim = models.DateTimeField(null=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    convidados = models.ManyToManyField(Convidado)

    def __str__(self):
        return f'{self.descricao} começa {self.data_inicio} até {self.data_fim}'

