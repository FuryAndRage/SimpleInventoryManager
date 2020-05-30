from django.contrib import admin
from .models import Baixa

@admin.register(Baixa)
class BaixaAdmin(admin.ModelAdmin):
	list_display = ('user','baixa_data','baixa_produto','baixa_quantidade',)
	search_fields = ('baixa_produto',)
