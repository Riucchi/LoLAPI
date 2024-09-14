from django.db import models

# Create your models here.

class Champion(models.Model):
    nombre = models.CharField(max_length=40)
    lore = models.TextField()
    champ_img = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.nombre


class Skill(models.Model):
    champion = models.ForeignKey(Champion, null=True, blank=True, on_delete=models.CASCADE, related_name='skills')
    passive_img = models.ImageField(upload_to='media/')
    q_img = models.ImageField(upload_to='media/')
    w_img = models.ImageField(upload_to='media/')
    e_img = models.ImageField(upload_to='media/')
    r_img = models.ImageField(upload_to='media/')
    passive_name = models.CharField(max_length=40, null=True, blank=True)
    q_name = models.CharField(max_length=40, null=True, blank=True)
    w_name = models.CharField(max_length=40, null=True, blank=True)
    e_name = models.CharField(max_length=40, null=True, blank=True)
    r_name = models.CharField(max_length=40, null=True, blank=True)


    def __str__(self):
        return self.passive_name

