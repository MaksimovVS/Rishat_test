from django.db import models


class Item(models.Model):
    """Экземпляр товара."""
    name = models.CharField(
        "Наименование",
        max_length=64,
        unique=True,
    )
    description = models.TextField(
        "Описание",
        max_length=1024,
    )
    price = models.IntegerField(
        "Цена",
        default=0
    )

    class Meta:
        verbose_name = "Экземпляр"
        verbose_name_plural = 'Экземпляры'

    def __str__(self):
        return f"{self.name}: {self.price}"
