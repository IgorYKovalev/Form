from django.urls import path
from form.views import FormFieldCreateView, index, index_detail, search

urlpatterns = [
    # path('get_form/', FormFieldView.as_view(), name='get_form'),
    path('get_form/', FormFieldCreateView.as_view(), name='get_form'),
    path('index/', index, name='index'),
    path('detail/<int:pk>/', index_detail, name='detail'),
    path('search/', search, name='search'),
]
