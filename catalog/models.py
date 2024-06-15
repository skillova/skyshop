from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание продукта",
    )
    image = models.ImageField(
        upload_to="products/images",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        related_name="Products",
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Цена за покупку",
        help_text="Введите цену продукта",
    )
    created_at = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания продукта",
    )
    updated_at = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату изменения продукта",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Пользователь',
        null=True,
        blank=True)

    class Meta:
        verbose_name = "Продукт"  # Настройка для наименования одного объекта
        verbose_name_plural = "Продукты"  # Настройка для наименования набора объектов
        ordering = ["category", "name"]

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.name} {self.description}"


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание категории",
    )

    class Meta:
        verbose_name = "Категория"  # Настройка для наименования одного объекта
        verbose_name_plural = "Категории"  # Настройка для наименования набора объектов

    def __str__(self):
        # Строковое отображение объекта
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    version = models.CharField(max_length=100, verbose_name="Версия")
    number_version = models.IntegerField(default=0, verbose_name="Номер версии")
    current_version = models.BooleanField(
        default=True, verbose_name="Признак текущей версии"
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"

    def __str__(self):
        return f"{self.number_version}"
