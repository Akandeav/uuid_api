from django.contrib import admin
from django.urls import path
from .views import UUIDView

urlpatterns = [
    path('uuids', UUIDView.as_view())
]