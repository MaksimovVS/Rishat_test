from django.db import models


class Item(models):
    """Экземпляр."""
    name = models.CharField(
        "Наименование",
        max_length=64,
    )
    description = models.TextField(
        "Описание",
        max_length=1024,
    )
    price = models.IntegerField(
        "Цена",
    )

    def __str__(self):
        return f"{self.name}: {self.price}"
