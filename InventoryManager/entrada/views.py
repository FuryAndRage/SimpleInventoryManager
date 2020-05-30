from django.shortcuts import render, get_object_or_404, redirect
from .models import Entrada
from .forms import EntradaForm
from django.views.generic.list import ListView
from InventoryManager.produto.models import Produto
from django.contrib import messages

class EntradaLogView(ListView):
	template_name = 'entrada_log.html'
	model = Entrada
	context_object_name = 'objects'
	ordering = '-entrada_data'


def entrada_produto(request, pk):
	prod = get_object_or_404(Produto, pk = pk)
	form = EntradaForm()
	

	if request.method == 'POST':
		form = EntradaForm(request.POST or None, instance = prod)
		if form.is_valid():
			dados = Entrada(
				user =request.user,
				entrada_produto = form.cleaned_data['entrada_produto'],
				entrada_quantidade = form.cleaned_data['entrada_quantidade'],
				entrada_motivo = form.cleaned_data['entrada_motivo'])
			if not dados.entrada_quantidade:
				dados.entrada_quantidade = 0
			if int(dados.entrada_quantidade) < 0:
				messages.error(request,'Valor da entrada nao pode ser menor que 0')
				return render(request, 'entrada_produto.html',{'form':form, 'produto':prod})
			prod.produto_quantidade += int(dados.entrada_quantidade)
			print(f'depois {prod.produto_quantidade}')
			prod.save()
			dados.save()
			messages.success(request,'Entrada do produto foi realizada com sucesso')
			return redirect('produto:list')
	else:
		return render(request, 'entrada_produto.html',{'form':form, 'produto':prod})
