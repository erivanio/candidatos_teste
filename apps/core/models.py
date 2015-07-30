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

    def is_front(self):
        if self.html >= 7 and self.css >= 7 and self.javascript >= 7:
            return True
        else:
            return False

    def is_back(self):
        if self.python >= 7 and self.django >= 7:
            return True
        else:
            return False

    def is_mobile(self):
        if self.ios >= 7 and self.android >= 7:
            return True
        else:
            return False

