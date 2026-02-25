from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('falcon/', include('dashboard.urls')),
]
