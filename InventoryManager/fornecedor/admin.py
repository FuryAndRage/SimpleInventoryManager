from django.contrib import admin
from . models import Fornecedor

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
	list_display = ('fornecedor_nome',)
	search_fields = ('fornecedor_nome',)
