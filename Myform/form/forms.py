from django import forms
from form.models import FormField


class FormFieldForm(forms.ModelForm):
    class Meta:
        model = FormField
        fields = ['name', 'name_field', 'type_field']
        widgets = {
            'name': forms.TextInput(attrs={'size': 27, 'placeholder': 'название не более 25 символов', 'class': 'form-control py-1'}),
            'name_field': forms.TextInput(attrs={'class': 'form-control py-1'}),
            'type_field': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 25:
            raise ValueError('Длина превышает 25 символов')
        return name
