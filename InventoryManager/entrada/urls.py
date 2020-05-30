from django.urls import path
from . import views

app_name = 'entrada'
urlpatterns = [
	path('log/', views.EntradaLogView.as_view(), name = 'log'),
	path('produto/<int:pk>/', views.entrada_produto, name = 'entrada')
]
