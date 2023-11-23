from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re


def is_valid_phone(value):
    if not re.match(r"^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$", value):
        raise ValidationError("Номер телефона должен быть в формате +7 xxx xxx xx xx")


def is_valid_date(value):
    if not re.match(r"^\d{4}-\d{2}-\d{2}$|^\d{2}\.\d{2}\.\d{4}$", value):
        raise ValidationError("Дата должна быть в формате DD.MM.YYYY или YYYY-MM-DD")


def is_valid_text(value):
    if not value.strip():
        raise ValidationError("Текстовое поле не может быть пустым")


is_valid_email = validate_email
