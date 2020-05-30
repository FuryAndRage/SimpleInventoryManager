from django.shortcuts import render, redirect, get_object_or_404
from InventoryManager.produto.models import Produto
from django.views.generic.list import ListView
from .forms import BaixaForm
from .models import Baixa
from django.contrib import messages

class BaixaView(ListView):
	model = Baixa
	template_name = 'baixa_log.html'
	context_object_name = 'objects'
	ordering = '-baixa_data'

def baixa_produto(request,pk):
	prod = get_object_or_404(Produto, pk=pk)
	form = BaixaForm()
	if not request.user.is_authenticated:
		messages.error(request, 'Voce precisa estar logado para realizar esta operacao')
		return redirect('produto:list')

	if request.method == 'POST':
		form = BaixaForm(request.POST or None, instance=prod)
		if form.is_valid():
			dados = Baixa(
				user = request.user,
				baixa_produto = form.cleaned_data['baixa_produto'],
				baixa_quantidade = form.cleaned_data['baixa_quantidade'],
				baixa_motivo = form.cleaned_data['baixa_motivo'],
				
				)
			
			if not dados.baixa_quantidade:
				dados.baixa_quantidade = 0
			if dados.baixa_quantidade == 0:
				messages.success(request,'Baixa igual a 0')
			if dados.baixa_quantidade < 0:
				messages.error(request, 'Valor da baixa nao pode ser menor que 0')
				return render(request, 'baixa_produto.html', {'form':form, 'produto':prod})
			if int(dados.baixa_quantidade) > prod.produto_quantidade:
				messages.error(request, 'Quantidade em estoque insuficiente')
				return render(request,'baixa_produto.html', {'form':form, 'produto':prod})
			prod.produto_quantidade -= int(dados.baixa_quantidade)
			dados.save()
			prod.save()
			messages.success(request, 'Baixa realizada com sucesso')
			return redirect('produto:list')
	else:
		return render(request,'baixa_produto.html', {'form':form, 'produto':prod})