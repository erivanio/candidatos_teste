from django.db import models

class Candidate(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField()
    html = models.IntegerField(null=True, blank=True)
    css = models.IntegerField(null=True, blank=True)
    javascript = models.IntegerField(null=True, blank=True)
    python = models.IntegerField(null=True, blank=True)
    django = models.IntegerField(null=True, blank=True)
    ios = models.IntegerField('Desenvolvimento IOS', null=True, blank=True)
    android = models.IntegerField('Desenvolvimento Android', null=True, blank=True)

    class Meta:
        verbose_name = 'Cadidato'
        verbose_name_plural = 'Candidatos'
