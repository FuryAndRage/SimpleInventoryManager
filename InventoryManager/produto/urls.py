from django.urls import path
from . import views

app_name = 'produto'
urlpatterns = [
	path('list/', views.ProdutoView.as_view(), name = 'list'),
	
]