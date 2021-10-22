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


class Product (models.Model):
    product_name=models.CharField(max_length=255)
    price=models.IntegerField()
    supermarket=models.CharField(max_length=255)

    class Meta:
        db_table = "product"

    def __str__(self):
        return (self.product_name + " " + str(self.price) + " " + self.supermarket)


    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(product_name__icontains=query) 
        )
        return object_list
