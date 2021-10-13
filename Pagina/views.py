from django.shortcuts import render, redirect
from Pagina.models import Usuarios

# Create your views here.

def login(request):
    if request.method == "GET":
        if request.session.get("nombre_usuario"):
            return redirect("index")
        else: 
            return render(request, 'login.html')
    if request.method == "POST":
        nusuario = request.POST.get("usuario")
        pusuario = request.POST.get("contra")
        usuario_actual=Usuarios.objects.filter(nombre_usuario=nusuario).exists()
        if usuario_actual:
            datos_usuario=Usuarios.objects.filter(nombre_usuario=nusuario).first()
            if getattr(datos_usuario,"password_usuario")==pusuario:
                request.session["nombredelusuario"]=getattr(datos_usuario, "nombre_usuario")
                request.session["nombre_completo_usuario"]=getattr(datos_usuario, "nombre_completo_usuario")
                return redirect("index")
            else:
                return render(request, 'login.html', {"mensaje_error":"Contraseña ingresada es incorrecta."})
        else:
            return render(request, 'login.html', {"mensaje_error":"Usuario ingresado no existe."})

def index(request):
    if request.session.get("nombredelusuario"):
        return render(request, 'index.html', {"nombre_usuario": request.session.get("nombre_completo_usuario")})
    else:
        return render(request, 'login.html')

def salir(request):
    request.session.flush()
    return redirect("./")   

def profile(request):
    return render (request, "profile.html")
 

