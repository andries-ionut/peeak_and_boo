from django.db import models

# Create your models here.

from django.db import models


class ProduseModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=False)
    price = models.DecimalField(max_digits=9)

    def __str__(self):
        return f"{self.name} - {self.description} - {self.price}"

