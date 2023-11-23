from django.contrib import admin
from form.models import FormField


@admin.register(FormField)
class FormFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_field', 'type_field')

