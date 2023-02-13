from django.db import models

CHOICES = (
    ("Rub", "Рублей"),
    ("usd", "Долларов"),
)


class Item(models.Model):
    """Модель товара"""

    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", max_length=1000)
    price = models.IntegerField(
        "Цена",
    )
    currency = models.CharField(
        "Валюта", choices=CHOICES, default="Rub", max_length=10
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def get_display_price(self):
        price = self.price / 100
        return price

    def get_display_currency(self):
        if self.currency == "Rub":
            return "₽"
        elif self.currency == "usd":
            return "$"

    def __str__(self) -> str:
        return self.name
