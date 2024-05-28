from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bebe_id>/', views.detalhes_bebe, name='detalhes_bebe'),
    path('adicionar/', views.adicionar_registro, name='adicionar_registro'),
]
