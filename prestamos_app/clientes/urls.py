from django.urls import path
from . import views

urlpatterns = [
    path('clientes/<int:interes>/', views.clientes_por_interes, name='clientes_por_interes'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
]