from django.db import models


class Letter(models.Model):
    letter = models.CharField(max_length=1)

    def __str__(self):
        return self.letter


class IrregularVerbs(models.Model):
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE)
    infinitive = models.CharField(max_length=100)
    preterit = models.CharField(max_length=100)
    past_participle = models.CharField(max_length=100)
    translation = models.CharField(max_length=200)

    def __str__(self):
        return f'Verbe {self.infinitive}'


class Fiche(models.Model):
    fiche = models.FileField(upload_to="fiche/")

    def __str__(self):
        return 'Pdf File'