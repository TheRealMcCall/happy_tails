from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=120,
        unique=True
    )
    slug = models.SlugField(
        max_length=120,
        unique=True
    )
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name
    