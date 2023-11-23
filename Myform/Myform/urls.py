from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from form.api import FormFieldViewSet

router = DefaultRouter()
router.register(r'get_form', FormFieldViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('form/', include('form.urls')),
]
