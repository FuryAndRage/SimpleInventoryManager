from django.db import models

class Fornecedor(models.Model):
	fornecedor_nome = models.CharField('Fornecedor',max_length=100)

	def __str__(self):
		return self.fornecedor_nome
