from django.urls import path
from .views import dashboard_page, pedidos_data, relatorios_page, gerar_word, revisar_texto

urlpatterns = [
    path("", dashboard_page),
    path("relatorio/", relatorios_page),
    path("gerar-word/", gerar_word),
    path("api/pedidos/", pedidos_data),
    path("api/revisar/", revisar_texto),
]
