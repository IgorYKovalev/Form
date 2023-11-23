from rest_framework.viewsets import ModelViewSet
from form.models import FormField
from form.serializers import FormFieldSerializer


class FormFieldViewSet(ModelViewSet):
    queryset = FormField.objects.all()
    serializer_class = FormFieldSerializer

    filterset_fields = [
        'name',
        'name_field',
        'type_field',
    ]
