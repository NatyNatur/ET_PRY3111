from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from appLex.models import Cliente
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate

def index(request):
    return render(request,"index.html")

def register(request):
    return render(request,"registro.html")

@csrf_protect
def registrar_cliente(request):
    rut = request.POST.get('inpRut')
    nombre = request.POST.get('inpNombre')
    appaterno = request.POST.get('inpApellidopa')
    apmaterno = request.POST.get('inpApellidoma')
    email =  request.POST.get('inpEmail')
    password = request.POST.get('inpPassword')
    
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
        mensaje = "Verifique datos ingresados, no se registró usuario."
    return render(request, 'registro.html', {'mensaje': mensaje})

def ingresar_app(request):
    email_recibido = request.POST.get('inpEmail')
    password_recibido = request.POST.get('inpPassword')
    cliente = Cliente.objects.filter(email = email_recibido).filter(password = password_recibido)
    if cliente:
        request.session['cliente'] = list(cliente.values())
        request.session.save()
        return redirect('inicio/')
        #return redirect('inicio/', usuario)
    else: 
        mensaje = "Usuario o contraseña incorrecta"
        return render(request, 'index.html', {'mensaje': mensaje})

# cliente
def home_cliente(request):
    cliente = request.session['cliente']
    return render(request, "cliente/vista_cliente.html", {'usuario': cliente})

def c_solicitudes(request):
    return render(request,"cliente/solicitud.html")

def c_contratos(request):
    return render(request,"cliente/contratos.html")

def modificar_cliente(request):
    cliente = request.session['cliente']
    return render (request, "cliente/modificar_cliente.html", {'usuario': cliente})

def modificacion_cliente(request):
    if request.POST.get("inpRut"):
        rut_recibido = request.POST.get("inpRut")
        nombre_recibido = request.POST.get("inpNombre")
        appaterno_recibido = request.POST.get("inpApellidopa")
        apmaterno_recibido = request.POST.get("inpApellidoma")
        email_recibido = request.POST.get("inpEmail")
        telefono_recibido = request.POST.get("inpTelefono")
        direccion_recibido = request.POST.get("inpDireccion")
        cliente = Cliente.objects.filter(rut = rut_recibido)
        if cliente:
            cli = Cliente.objects.get(rut = rut_recibido)
            cli.nombre = nombre_recibido
            cli.appaterno = appaterno_recibido
            cli.apmaterno = apmaterno_recibido
            cli.telefono = telefono_recibido
            cli.direccion = direccion_recibido
            cli.email = email_recibido
            cli.save()
            request.session['cliente'] = list(cliente.values())
            request.session.save()
            mensaje = "Datos correctamente modificados."           
        else:
            mensaje = "No existe usuario a modificar."           
    else:
        mensaje = "Ha ocurrido un error, no contamos con la información para modificar."
    return redirect('/inicio/')

# abogado
def home_abogado(request):
    return render(request, "abogado/vista_abogado.html")

def a_presupuestos(request):
    return render(request, "abogado/presupuestos.html")

def a_det_presupuesto(request):
    return render(request, "abogado/presupuesto_detalle.html")

def a_causas(request):
    return render(request, "abogado/causas.html")

# técnico jurídico
def home_tecjuridico(request):
    return render(request, "tj/vista_tecnico.html")

def tj_solicitudes(request):
    return render(request, "tj/solicitudes.html")

def tj_registrar_pagos(request):
    return render(request, "tj/registrar_pagos.html")
