from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from .routers import router

from django.views.generic import TemplateView

urlpatterns = [
    path('api/', include(router.urls)),
    path('inv/', TemplateView.as_view(template_name='index.html')),
]

