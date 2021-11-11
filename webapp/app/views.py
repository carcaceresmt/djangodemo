from django.shortcuts import render

# Create your views here.
from app.forms import calculadoraForm, rectanguloForm, formulaForm
from app.funciones.Calculo import sumarnumero, areaRectangulo, formula


def sumarPeticion(request):
    suma=0
    if(request.method=="POST"):
        form = calculadoraForm(request.POST)
        if form.is_valid():
            n1 = float(form.data['n1'])
            n2 = float(form.data['n2'])
            suma= sumarnumero(n1, n2)
    else:
        form = calculadoraForm()

    return render(request, 'calcular.html', {'form': form, 'suma': suma})

def areaPeticion(request):
    area=0
    if(request.method=="POST"):
        form = rectanguloForm(request.POST)
        if form.is_valid():
           base= float(form.data['base'])
           altura= float(form.data['altura'])
           area= areaRectangulo(base,altura)
    else:
        form = rectanguloForm()

    return render(request, 'area.html', {'form': form, 'area': area})

def formulaPeticion(request):
    resultado=0
    if(request.method=="POST"):
        form = formulaForm(request.POST)
        if form.is_valid():
           x= float(form.data['x'])
           y= float(form.data['y'])
           z = float(form.data['z'])
           resultado= formula(x, y, z)
    else:
        form = formulaForm()

    return render(request, 'formula.html', {'form': form, 'resultado': resultado})

