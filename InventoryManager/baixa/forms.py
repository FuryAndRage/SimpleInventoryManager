from django import forms
from .models import Baixa
from django.forms.widgets import HiddenInput

class BaixaForm(forms.ModelForm):
	class Meta:
		model = Baixa
		fields = '__all__'
		widgets = {'user':forms.HiddenInput()}