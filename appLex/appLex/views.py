from asyncio.windows_events import NULL
from django.shortcuts import render
from appLex.models import Cliente
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def register(request):
    return render(request,"registro.html")

def registrar_cliente(request):
    rut = request.GET["inpRut"]
    nombre = request.GET["inpNombre"]
    appaterno = request.GET["inpApellidopa"]
    apmaterno = request.GET["inpApellidoma"]
    email = request.GET["inpEmail"]
    password = request.GET["inpPassword"]
    if len(nombre) > 0 and len(rut) > 0 and len(appaterno) > 0 and len(apmaterno) > 0:
        cliente = Cliente(rut = rut, 
        nombre = nombre, 
        appaterno = appaterno, 
        apmaterno = apmaterno,
        email = email,
        password = password)
        cliente.save()
        mensaje = "Cliente registrado exitosamente."
    else:
        mensaje = "Verifique datos ingresados, no se registró."
    return render(request, "index.html", {'mensaje':mensaje})

def home_cliente(request):
    return render(request, "cliente/vista_cliente.html")