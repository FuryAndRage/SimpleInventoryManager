from django.db import models
from InventoryManager.fornecedor.models import Fornecedor

class Produto(models.Model):
	produto_fornecedor = models.ForeignKey(Fornecedor, on_delete = models.CASCADE, verbose_name='Fornecedor')
	produto_nome = models.CharField('Produto', max_length=100)
	produto_preco = models.FloatField(null=True)
	produto_quantidade = models.IntegerField()
	produto_descricao = models.TextField(null=True)
	produto_imagem = models.ImageField(upload_to='produtos/%Y/%m',null=True)


	def __str__(self):
		return self.produto_nome
