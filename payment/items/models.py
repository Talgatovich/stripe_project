from django.db import models


class Item(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", max_length=1000)
    price = models.IntegerField(
        "Цена",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return self.name
