from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Описание",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
        related_name="Products"
    )
    image = models.ImageField(
        upload_to="products/images",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
    )
    category = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите категорию продукта"
    )
    price = models.FloatField(
        blank=False,
        null=False,
        verbose_name="Цена за покупку",
        help_text="Введите цену продукта",
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания продукта",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату изменения продукта",
    )
    manufactured_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата производства продукта",
        help_text="Введите дату производства продукта",
    )

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
        verbose_name="Описание",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"  # Настройка для наименования одного объекта
        verbose_name_plural = "Категории"  # Настройка для наименования набора объектов

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.name} {self.description}"
