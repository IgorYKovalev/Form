import logging
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from .forms import FormFieldForm
from .models import FormField
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

log = logging.getLogger(__name__)


def search(request):
    query = request.GET.get('q')
    if query:
        results = FormField.objects.filter(Q(name__icontains=query) | Q(name_field__icontains=query))
        context = {
            'results': results,
        }
        return render(request, 'form/search_results.html', context=context)
    return render(request, 'form/index.html')


def index(request):
    context = {
        'list_form': FormField.objects.all()
    }
    log.info('Рендер страницы index')
    return render(request, 'form/index.html', context=context)


def index_detail(request, pk):
    detail_form = get_object_or_404(FormField, pk=pk)
    context = {
        'detail_form': detail_form,
    }
    log.info('Рендер страницы detail')
    return render(request, 'form/index_detail.html', context=context)


class FormFieldCreateView(CreateView):
    log.info('Рендер страницы Form')
    model = FormField
    form_class = FormFieldForm
    success_url = reverse_lazy('index')


# class FormFieldView(View):
#     def get(self, request):
#         form = FormFieldForm()
#         return render(request, 'form/index.html', {'form': form})
#
#     def post(self, request):
#         if request.method == 'POST':
#             form = FormFieldForm(request.POST)
#             if form.is_valid():
#                 # FormField.objects.create(**form.cleaned_data)
#                 form.save()
#                 return HttpResponse(f'Форма заполнена')
#                 # name = form.cleaned_data['name']
#                 # name_field = form.cleaned_data['name_field']
#                 # type_field = form.cleaned_data['type_field']
#                 # return HttpResponse(f'Вы заполнили {name}, {name_field}, {type_field}')
#             return render(request, 'form/index.html', {'form': form})






