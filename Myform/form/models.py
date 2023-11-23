from django.db import models
from form.validators import is_valid_phone, is_valid_date, is_valid_email, is_valid_text


class FormField(models.Model):
    class Type(models.TextChoices):
        EMAIL = 'email', 'Почта'
        DATE = 'date', 'Дата'
        PHONE = 'phone', 'Телефон'
        TEXT = 'text', 'Текст'

    name = models.CharField(max_length=256, verbose_name='Название шаблона')
    name_field = models.CharField(max_length=256, verbose_name='Имя поля')
    type_field = models.CharField(max_length=5, choices=Type.choices, verbose_name='Тип поля')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'

    def clean(self):
        if "date" in self.type_field:
            is_valid_date(self.name_field)

        elif "phone" in self.type_field:
            is_valid_phone(self.name_field)

        elif "email" in self.type_field:
            is_valid_email(self.name_field)

        else:
            is_valid_text(self.name_field)
