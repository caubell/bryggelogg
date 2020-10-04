from django.db import models
from django.urls import reverse


class Recipes(models.Model):
    name = models.CharField(max_length = 264)
    type = models.CharField(max_length = 264)
    date = models.DateField(blank = True, null = True,)
    og = models.FloatField(blank = True, null = True)
    fg = models.FloatField(blank = True, null = True,)
    abv = models.FloatField(blank = True, null = True,)
    ibu = models.FloatField(blank = True, null = True,)
    efficiency = models.FloatField(blank = True, null = True,)
    batch_volume = models.FloatField(blank = True, null = True)
    mash_time = models.IntegerField(blank = True, null = True)
    boil_time = models.IntegerField(blank = True, null = True)
    mash_temp = models.IntegerField(blank = True, null = True)
    boil_volume = models.FloatField(blank = True, null = True,)
    fermenter_volume = models.FloatField(blank = True, null = True,)
    yeast = models.CharField(blank = True, null = True, max_length = 264)
    link = models.CharField(blank = True, null = True, max_length = 264)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Bryggelogg:detail', kwargs = {'pk': self.pk})

class Malt(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.PROTECT)
    malt = models.CharField(max_length = 264)
    amount = models.IntegerField()

    def __str__(self):
        return self.malt

class Hop(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.PROTECT)
    hop = models.CharField(max_length = 264)
    amount = models.IntegerField()

    def __str__(self):
        return self.hop

class Bryggelogg(models.Model):
    bryggnr = models.IntegerField(blank = True, null = True,)
    navn = models.CharField(blank = True, null = True, max_length = 264)
    dato = models.DateField(blank = True, null = True,)
    og = models.FloatField(blank = True, null = True)
    fg = models.FloatField(blank = True, null = True,)
    abv = models.FloatField(blank = True, null = True,)
    effektivitet = models.FloatField(blank = True, null = True,)
    sluttvolum = models.FloatField(blank = True, null = True)
    utbytte = models.FloatField(blank = True, null = True)
    mesketemperatur = models.IntegerField(blank = True, null = True)
    rating = models.IntegerField(blank = True, null = True,)
    meskevann = models.FloatField(blank = True, null = True,)
    kokevolum = models.FloatField(blank = True, null = True,)
    etterfylling = models.FloatField(blank = True, null = True,)
    gjaer = models.CharField(blank = True, null = True, max_length = 264)
    kommentar = models.TextField(blank = True, null = True)
    malt_1 = models.CharField(blank = True, max_length = 264)
    m_mengde_1 = models.FloatField(blank = True, null = True)
    malt_2 = models.CharField(blank = True, max_length = 264)
    m_mengde_2 = models.FloatField(blank = True, null = True)
    malt_3 = models.CharField(blank = True, max_length = 264)
    m_mengde_3 = models.FloatField(blank = True, null = True)
    malt_4 = models.CharField(blank = True, max_length = 264)
    m_mengde_4 = models.FloatField(blank = True, null = True)
    malt_5 = models.CharField(blank = True, max_length = 264)
    m_mengde_5 = models.FloatField(blank = True, null = True)
    humle_1 = models.CharField(blank = True, max_length = 264)
    h_mengde_1 = models.FloatField(blank = True, null = True)
    humle_2 = models.CharField(blank = True, max_length = 264)
    h_mengde_2 = models.FloatField(blank = True, null = True)
    humle_3 = models.CharField(blank = True, max_length = 264)
    h_mengde_2 = models.FloatField(blank = True, null = True)
    humle_3 = models.CharField(blank = True, max_length = 264)
    h_mengde_3 = models.FloatField(blank = True, null = True)
    humle_4 = models.CharField(blank = True, max_length = 264)
    h_mengde_4 = models.FloatField(blank = True, null = True)
    humle_5 = models.CharField(blank = True, max_length = 264)
    h_mengde_5 = models.FloatField(blank = True, null = True)

    def __str__(self):
        return self.navn

    def get_absolute_url(self):
        return reverse('Bryggelogg:detail', kwargs = {'pk': self.pk})
