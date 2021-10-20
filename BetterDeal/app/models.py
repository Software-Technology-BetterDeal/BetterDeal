from django.db import models

# Create your models here.

class DummyDatabase(models.Model):
    name= models.CharField(max_length=255)
    price=models.IntegerField()

    class Meta:
        verbose_name_plural = "Dummies"

    def __str__(self):
        return (self.name + " " + str(self.price))



	
