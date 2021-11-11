from django.forms import ModelForm, TextInput

from app.models import Calculadora, rectangulo, Formula


class calculadoraForm(ModelForm):
    class Meta:
        model = Calculadora
        fields='__all__'
        widgets={
            'n1':TextInput(attrs={'type': 'number', 'value': '0'}),
            'n2': TextInput(attrs={'type': 'number', 'value': '0'})
        }

class rectanguloForm(ModelForm):
    class Meta:
        model = rectangulo
        fields= '__all__'
        widgets= {
            'base': TextInput(attrs={'type': 'number', 'value': '0'}),
            'altura': TextInput(attrs={'type': 'number', 'value': '0'})
        }


class formulaForm(ModelForm):
    class Meta:
        model = Formula
        fields= '__all__'
        widgets= {
            'x': TextInput(attrs={'type': 'number', 'value': '0'}),
            'y': TextInput(attrs={'type': 'number', 'value': '0'}),
            'z': TextInput(attrs={'type': 'number', 'value': '0'})
        }