from django.shortcuts import render,redirect,get_object_or_404
from . models import Produto
from InventoryManager.baixa.models import Baixa
from InventoryManager.baixa.forms import BaixaForm
from django.views.generic.list import ListView

class ProdutoView(ListView):
	template_name = 'produto_list.html'
	context_object_name = 'objects'
	model = Produto

