from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.title}'
