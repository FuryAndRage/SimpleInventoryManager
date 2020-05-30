from django.contrib import admin
from .models import Entrada

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
	list_display = ('user', 'entrada_data', 'entrada_produto','entrada_quantidade')
	search_fields = ('entrada_produto',)
