from django.shortcuts import redirect, render
from django.http import HttpResponse
from crud.models import Persona as PersonaModel

# Create your views here.
def index(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def crud_index(request):
    no_registers = PersonaModel.objects.count()
    registers = PersonaModel.objects.all()
    return render(request, 'persona_crud/index.html',{'no_registers':no_registers, 'registers':registers})

def crud_create(request):
    return render(request, 'persona_crud/create.html')

def crud_store(request):
    if request.method == 'POST':
        dato = request.POST
        new_persona = PersonaModel(nombre=dato["nombre"],apellido=dato["apellido"],email=dato["email"])
        new_persona.save()
        return redirect("crud_index")

def crud_edit(request,id):
    register = PersonaModel.objects.get(pk=id)
    return render(request, 'persona_crud/edit.html',{'register':register})

def crud_update(request,id):
    if request.method == 'POST':
        dato = request.POST
        persona = PersonaModel.objects.get(pk=id)
        persona.nombre = dato["nombre"]
        persona.apellido = dato["apellido"]
        persona.email = dato["email"]
        persona.save()
        return redirect("crud_index")

def crud_delete(request,id):
    register_persona = PersonaModel.objects.get(pk=id)
    register_persona.delete()
    return redirect("crud_index")
