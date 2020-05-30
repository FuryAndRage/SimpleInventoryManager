from django.urls import path
from . import views

app_name = 'baixa'
urlpatterns = [
path('log/', views.BaixaView.as_view(), name='log'),
path('produto/<int:pk>/',views.baixa_produto, name='baixa'),
]