from django.db import models
from InventoryManager.produto.models import Produto
from django.contrib.auth.models import User

class Baixa(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE,null=True)
	baixa_data = models.DateTimeField(auto_now=True,verbose_name='Data')
	baixa_produto = models.ForeignKey(Produto, on_delete = models.CASCADE, verbose_name='Baixa')
	baixa_quantidade = models.IntegerField(verbose_name='Quantidade')
	baixa_motivo = models.TextField(verbose_name='Motivo')

	def __str__(self):
		return str(self.baixa_produto)
