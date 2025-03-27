from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.TextField(max_length=255, verbose_name="nombre")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    description = models.TextField(max_length=300, verbose_name="descripción")
    available = models.BooleanField(default=True, verbose_name="disponible")
    photo = models.ImageField(
        upload_to="logos", null=True, blank=True, verbose_name="foto"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name="creado el"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="actualizado el")

    def __str__(self):
        return self.name
