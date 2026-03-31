from django.urls import path
from .views import dashboard_page, xcp_data, revisar_ia, gerar_word, editor_page

urlpatterns = [
    path("", dashboard_page, name="dashboard"),
    path("editor/", editor_page, name="editor"),
    path("api/pedidos/", xcp_data, name="xcp_data"),
    path('revisar/', revisar_ia, name="revisar_ia"),
    path('gerar-word/', gerar_word, name="gerar_word"),
]
