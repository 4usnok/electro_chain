from django.db import models

class ContactsFactory(models.Model):
    """Модель для контактов"""
    email_cont = models.EmailField(
        max_length=254,
        help_text="Почта завода",
    )
    country_cont = models.CharField(
        max_length=100,
        help_text="Страна",
    )
    city_cont = models.CharField(
        max_length=100,
        help_text="Город",
    )
    street_cont = models.CharField(
        max_length=100,
        help_text="Улица",
    )
    number_phone_cont = models.CharField(
        max_length=20,
        help_text="Номер телефона"
    )

    def __str__(self):
        return self.email_cont

class ProductsFactory(models.Model):
    """Модель для продукта"""
    name_pr = models.CharField(
        max_length=100,
        help_text="Название продукта",
    )
    models_pr = models.CharField(
        max_length=100,
        help_text="Название модели",
    )
    release_pr = models.DateField(
        help_text="Дата выхода продукта",
    )

    def __str__(self):
        return self.name_pr

class Network(models.Model):
    """Модель для сети"""

    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]
    level = models.IntegerField(
        choices=LEVEL_CHOICES,
        verbose_name="factory_level",
        help_text="звенья"
    )

    name_fact = models.CharField(
        max_length=30,
        help_text="Название завода",
    )
    contacts_fact = models.ForeignKey(
        ContactsFactory,
        on_delete=models.CASCADE,
        help_text="Контакты завода",
    )
    products_fact = models.ManyToManyField(
        ProductsFactory,
        help_text="Продукты",
    )
    supplier_fact = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Поставщик",
    )
    debt_fact = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        help_text="Задолженность с точностью до копеек",
        null=True,
        blank=True,
    )
    time_create_fact = models.TimeField(
        auto_now_add=True,
        help_text="Время заполнения",
    )

    def __str__(self):
        return self.name_fact

    class Meta:
        ordering = [
            'debt_fact',
        ]
