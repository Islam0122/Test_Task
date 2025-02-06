from django.db import models
from django.contrib.auth.models import User

# BaseModel -> Базовая модель
class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания записи"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
        help_text="Дата и время последнего обновления"
    )

    class Meta:
        abstract = True


# Category -> Категории
class Category(BaseModel):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Название категории",
        help_text="Введите название категории"
    )
    icon = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True,
        verbose_name="Иконка",
        help_text="Загрузите изображение для категории (необязательно)"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


# Product -> Объявления
class Product(BaseModel):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
        help_text="Введите название объявления"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание объявления"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        help_text="Введите стоимость объявления"
    )
    currency = models.CharField(
        max_length=3,
        choices=[("USD", "$"), ("KGS", "сом")],
        default="USD",
        verbose_name="Валюта",
        help_text="Выберите валюту (USD или KGS)"
    )
    location = models.CharField(
        max_length=255,
        verbose_name="Местоположение",
        help_text="Укажите местоположение объявления"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
        help_text="Выберите категорию для объявления"
    )
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите изображение объявления (необязательно)"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Владелец",
        help_text="Пользователь, разместивший объявление"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


# Favorite -> Избранное
class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name="Пользователь",
        help_text="Пользователь, добавивший продукт в избранное"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name="Объявление",
        help_text="Продукт, добавленный в избранное"
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления",
        help_text="Дата и время добавления в избранное"
    )

    class Meta:
        unique_together = ["user", "product"]
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"
        ordering = ["-added_at"]

    def __str__(self):
        return f"Избранное от {self.user} - {self.product.title}"

