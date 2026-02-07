from django.urls import path
from .views import dashboard_page, pedidos_data

urlpatterns = [
    path("", dashboard_page),
    path("api/pedidos/", pedidos_data),
]
