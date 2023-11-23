from rest_framework import serializers
from .models import FormField
from .validators import is_valid_date, is_valid_phone, is_valid_email, is_valid_text


class FormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormField
        fields = ['name', 'name_field', 'type_field']

    def validate(self, data):
        if 'date' in data['type_field']:
            is_valid_date(data['name_field'])

        elif 'phone' in data['type_field']:
            is_valid_phone(data['name_field'])

        elif 'email' in data['type_field']:
            is_valid_email(data['name_field'])

        else:
            is_valid_text(data['name_field'])

        return data
