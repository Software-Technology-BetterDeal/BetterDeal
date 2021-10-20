from django.db import models

from django.db.models import Q

# Create your models here.

class DummyDatabase(models.Model):
    name= models.CharField(max_length=255)
    price=models.IntegerField()


    class Meta:
        verbose_name_plural = "Dummies"

    def __str__(self):
        return (self.name + " " + str(self.price))

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = DummyDatabase.objects.filter(
            Q(name__icontains=query) 
        )
        return object_list



	
