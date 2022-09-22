from django.db import models
from django.shortcuts import  reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=10)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_productes(cls):
        return cls.objects.all()


    def get_show_url(self):
        return reverse("products.show", args=[self.id])

    @staticmethod
    def get_index_url():
        return reverse("products.index")

    def get_edit_url(self):
        return reverse("products.edit", args=[self.id])

    def get_delete_url(self):
        return reverse("products.delete", args=[self.id])