from django.db import models
from InventoryManager.produto.models import Produto
from django.contrib.auth.models import User

class Entrada(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	entrada_produto = models.ForeignKey(Produto, on_delete = models.CASCADE, verbose_name='Produto')
	entrada_data = models.DateTimeField(auto_now=True)
	entrada_quantidade = models.IntegerField()
	entrada_motivo = models.TextField()

	def __str__(self):
		return self.entrada_produto


