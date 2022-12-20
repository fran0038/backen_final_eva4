from django import forms

class Ventas(forms,Form):

    nombre = forms.CharField()
    