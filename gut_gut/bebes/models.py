from django.db import models

class Bebe(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    peso = models.FloatField()
    altura = models.FloatField()
    grupo_sanguineo = models.CharField(max_length=3)

class Alimentacao(models.Model):
    bebe = models.ForeignKey(Bebe, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    tipo = models.CharField(max_length=100)
    quantidade = models.IntegerField()

class TrocaDeFralda(models.Model):
    bebe = models.ForeignKey(Bebe, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    tipo = models.CharField(max_length=100)
    observacoes = models.TextField()

class Sono(models.Model):
    bebe = models.ForeignKey(Bebe, on_delete=models.CASCADE)
    data_hora_inicio = models.DateTimeField()
    data_hora_fim = models.DateTimeField()
    qualidade = models.CharField(max_length=100)

class ConsultaMedica(models.Model):
    bebe = models.ForeignKey(Bebe, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    medico = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    observacoes = models.TextField()

