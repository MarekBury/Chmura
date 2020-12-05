from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=80, null=True)
    password = models.CharField(max_length=80, null=True)
    email = models.CharField(max_length=80, null=True)
    telefon = models.CharField(max_length=80, null=True)
    data_utworzenia = models.DateTimeField(auto_now_add=True, null=True)
    age = models.IntegerField() 
    
    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=80, null=True)
    
    def __str__(self):
        return self.name

class Produkt(models.Model):
    KATEGORIA = (
        ('Domowe', 'Domowe'),
        ('Zewnętrzne', 'Zewnętrzne'),
    )

    nazwa = models.CharField(max_length=80, null=True)
    cena = models.FloatField(null = True)
    kategoria = models.CharField(max_length=80, null=True, choices= KATEGORIA)
    opis = models.CharField(max_length=80, null=True, blank=True)
    data_utworzenia = data_utworzenia = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.nazwa



class Zamowienie(models.Model):
    STATUS = (
        ('Oczekiwanie', 'Oczekiwanie'),
        ('W doręczeniu', 'W doręczeniu'),
        ('Dostarczono', 'Dostarczono'),
    )

    klient = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    produkt = models.ForeignKey(Produkt, null=True, on_delete=models.SET_NULL)
    data_utworzenia = data_utworzenia = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=80, null=True, choices = STATUS)
    
    def __str__(self):
        return self.produkt.nazwa