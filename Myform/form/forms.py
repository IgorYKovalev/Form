from django import forms
from form.models import FormField


class FormFieldForm(forms.ModelForm):
    class Meta:
        model = FormField
        fields = ['name', 'name_field', 'type_field']
        widgets = {
            'name': forms.TextInput(attrs={'size': 27, 'placeholder': 'название не более 25 символов'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 25:
            raise ValueError('Длина превышает 25 символов')
        return name



