from django import forms
from .models import Entrada
from django.forms.widgets import HiddenInput
class EntradaForm(forms.ModelForm):
	class Meta:
		model = Entrada
		fields = '__all__'
		widgets = {'user':forms.HiddenInput()}