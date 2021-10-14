from django.shortcuts import render, redirect
from pagina.models import usuarios

# Create your views here.
def login(request):
    if request.method=="GET":
        if request.session.get("cod_usuario"):
            return redirect("inicio")
        else:
            return render(request, 'login.html')

    if request.method=="POST":
        v_usuario=request.POST.get("usuario")
        v_clave=request.POST.get("clave")
        usuario_actual=usuarios.objects.filter(usuario=v_usuario).exists()
        if usuario_actual:
            datos_usuario=usuarios.objects.filter(usuario=v_usuario).first()
            if getattr(datos_usuario,"clave")==v_clave:
                request.session["cod_usuario"]=getattr(datos_usuario, "cod_usuario")
                request.session["nombre_completo"]=getattr(datos_usuario, "nombre_completo")
                return redirect("inicio")
            else:
                return render(request, 'login.html', {"mensaje_error":"La clave no corresponde"})
        else:
            return render(request, 'login.html', {"mensaje_error":"El usuario no existe"})

def salir(request):
    request.session.flush()
    return redirect("login")

def inicio(request):
    return render(request, 'inicio.html', {"nombre_completo":request.session.get("nombre_completo"), "titulo_f":"Inicio", "subtitulo_f":"Sistema de prueba desarrollado en el framework Django con Python"})

def acerca(request):
    return render(request, 'acerca.html')

def verusuario(request):
    if request.session.get("cod_usuario"):
        listatabla=usuarios.objects.all()
        return render(request, "usuarios/verusuario.html", {"nombre_completo":request.session.get("nombre_completo"), "titulo_f":"Usuarios", "subtitulo_f":"Listado de Usuarios registrados", "listatabla":listatabla})
    else:
        return redirect("login")

def modusuario(request,usu_actual=0):
    if request.session.get("cod_usuario"):
        if request.method=="GET":
            usuario_actual=usuarios.objects.filter(cod_usuario=usu_actual).exists()
            if usuario_actual:
                datos_usuario=usuarios.objects.filter(cod_usuario=usu_actual).first()
                return render(request, "usuarios/modusuario.html", {"nombre_completo":request.session.get("nombre_completo"), "titulo_f":"Modificar Usuario", "subtitulo_f":"Vuleva a escribir los datos que desea modificar", "datos_act":datos_usuario, "usu_actual":usu_actual})
            else:
                return render(request, "usuarios/modusuario.html", {"nombre_completo":request.session.get("nombre_completo"), "titulo_f":"Nuevo Usuario", "subtitulo_f":"Por favor complete todos los datos solicitados", "usu_actual":usu_actual})

        if request.method=="POST":
            if usu_actual==0:
                usuario_nuevo=usuarios(usuario=request.POST.get('usuario'), clave=request.POST.get('clave'), nombre_completo=request.POST.get('nombre_completo'))
                usuario_nuevo.save()
            else:
                usuario_actual=usuarios.objects.get(cod_usuario=usu_actual)
                usuario_actual.nombre_completo=request.POST.get('nombre_completo')
                usuario_actual.usuario=request.POST.get('usuario')
                usuario_actual.clave=request.POST.get('clave')
                usuario_actual.save()

            return redirect('verusuario')
    else:
        return redirect("login")

def borusuario(request, usu_actual):
    if request.session.get("cod_usuario"):
        usuarios.objects.filter(cod_usuario=usu_actual).delete()
        return redirect('verusuario')
    else:
        return redirect("login")
