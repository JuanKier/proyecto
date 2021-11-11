from django.shortcuts import render, redirect
from Pagina.models import *

# Create your views here.

def login(request):
    if request.method == "GET":
        if request.session.get("id_usuario"):
            return redirect("index")
        else: 
            return render(request, 'login.html')
    if request.method == "POST":
        nusuario = request.POST.get("usuario")
        pusuario = request.POST.get("contra")
        usuario_actual=Usuario.objects.filter(nombre_usuario=nusuario).exists()
        if usuario_actual:
            datos_usuario=Usuario.objects.filter(nombre_usuario=nusuario).first()
            if getattr(datos_usuario,"password_usuario")==pusuario:
                request.session["id_usuario"]=getattr(datos_usuario, "id_usuario")
                request.session["nombre_completo_usuario"]=getattr(datos_usuario, "nombre_completo_usuario")
                return redirect("index")
            else:
                return render(request, 'login.html', {"mensaje_error":"Contraseña ingresada es incorrecta."})
        else:
            return render(request, 'login.html', {"mensaje_error":"Usuario ingresado no existe."})

def index(request):
    return validar(request, "index.html")

def salir(request):
    request.session.flush()
    return redirect("./")   

def profile(request):
    return validar(request, "profile.html")

def products(request):
    return validar(request, "products.html")    

def clients(request):
    return validar(request, "clients.html") 

def users(request):
    return validar(request, "users.html") 

def verusuario(request):
    if request.session.get("id_usuario"):
        listatabla=Usuario.objects.all()
        return render(request, "users/verusuario.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Usuarios", "subtitulo_f":"Listado de Usuarios registrados", "listatabla":listatabla})
    else:
        return redirect("login")

def modusuario(request,usu_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            usuario_actual=Usuario.objects.filter(id_usuario=usu_actual).exists()
            if usuario_actual:
                datos_usuario=Usuario.objects.filter(id_usuario=usu_actual).first()
                return render(request, "users/modusuario.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Usuario", 
                "subtitulo_f":"Vuleva a escribir los datos que desea modificar", 
                "datos_act":datos_usuario, 
                "usu_actual":usu_actual})
            else:
                return render(request, "users/modusuario.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Nuevo Usuario", "subtitulo_f":"Por favor complete todos los datos solicitados", "usu_actual":usu_actual})

        if request.method=="POST":
            if usu_actual==0:
                usuario_nuevo=Usuario(nombre_usuario=request.POST.get('nombre_usuario'), password_usuario=request.POST.get('password_usuario'), nombre_completo_usuario=request.POST.get('nombre_completo_usuario'))
                usuario_nuevo.save()
            else:
                usuario_actual=Usuario.objects.get(id_usuario=usu_actual)
                usuario_actual.nombre_completo_usuario=request.POST.get('nombre_completo_usuario')
                usuario_actual.nombre_usuario=request.POST.get('nombre_usuario')
                usuario_actual.password_usuario=request.POST.get('password_usuario')
                usuario_actual.save()

            return redirect('verusuario')
    else:
        return redirect("login")

def borusuario(request, usu_actual):
        Usuario.objects.filter(id_usuario=usu_actual).delete()
        return redirect('verusuario')
 
 
def validar (request, pageSuccess):
    if request.session.get("id_usuario"):
        return render(request, pageSuccess, {"nombre_usuario": request.session.get("nombre_completo_usuario")})
    else:
        return render(request, 'login.html')

