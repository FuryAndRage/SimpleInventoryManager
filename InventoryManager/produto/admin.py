from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('produto_fornecedor','produto_nome','produto_quantidade',)
	search_fields = ('produto_nome',)
