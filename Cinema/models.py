from django.db import models

# Create your models here.

class Zhanr(models.Model):
    type = models.CharField(max_length=50)
    kino = models.ForeignKey('Kino', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.type
    
    
class Kino(models.Model):
    name = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
    price = models.CharField(max_length=1000)
    image = models.ImageField()
    
    def __str__(self):
        return self.name
    
    
class Fidbek(models.Model):
    otziv = models.CharField(max_length=500)
    
    def __str__(self):
        return self.otziv