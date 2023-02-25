from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()



class Team(models.Model):
    namE = models.CharField(max_length=250)
    imge = models.ImageField(upload_to='pics')
    desC = models.TextField()

    def __str__(self):
        return self.name
