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
                request.session["tipo_usuario"]=getattr(datos_usuario, "tipo_usuario")
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

def proveedor(request):
    return validar(request, "proveedor.html")

def inventario(request):
    return validar(request, "inventario.html")

#--=======================================Usuario======================================--

def verusuario(request):
    if request.session.get("id_usuario"):
        listatabla=Usuario.objects.all()
        return validar(request, "users/verusuario.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Usuarios", "subtitulo_f":"Listado de Usuarios registrados", "listatabla":listatabla})
    else:
        return redirect("login")

def modusuario(request,usu_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            usuario_actual=Usuario.objects.filter(id_usuario=usu_actual).exists()
            if usuario_actual:
                datos_usuario=Usuario.objects.filter(id_usuario=usu_actual).first()
                return validar(request, "users/modusuario.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Usuario", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_usuario, 
                "usu_actual":usu_actual})
            else:
                return validar(request, "users/modusuario.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Nuevo Usuario", "subtitulo_f":"Por favor complete todos los datos solicitados", "usu_actual":usu_actual})

        if request.method=="POST":
            if usu_actual==0:
                usuario_nuevo=Usuario(nombre_usuario=request.POST.get('nombre_usuario'), 
                password_usuario=request.POST.get('password_usuario'), 
                nombre_completo_usuario=request.POST.get('nombre_completo_usuario'), 
                tipo_usuario=request.POST.get('tipo_usuario'), 
                ci_usuario=request.POST.get('ci_usuario'), 
                telefono_usuario=request.POST.get('telefono_usuario'), 
                direccion_usuario=request.POST.get('direccion_usuario'))
                
                usuario_nuevo.save()
            else:
                usuario_actual=Usuario.objects.get(id_usuario=usu_actual)
                usuario_actual.nombre_completo_usuario=request.POST.get('nombre_completo_usuario')
                usuario_actual.nombre_usuario=request.POST.get('nombre_usuario')
                usuario_actual.password_usuario=request.POST.get('password_usuario')
                usuario_actual.tipo_usuario=request.POST.get('tipo_usuario')
                usuario_actual.ci_usuario=request.POST.get('ci_usuario')
                usuario_actual.telefono_usuario=request.POST.get('telefono_usuario')
                usuario_actual.direccion_usuario=request.POST.get('direccion_usuario')
                usuario_actual.save()

            return redirect('verusuario')
    else:
        return redirect("login")

def borusuario(request, usu_actual):
        Usuario.objects.filter(id_usuario=usu_actual).delete()
        return redirect('verusuario')

#--=======================================Cliente======================================--

def vercliente(request):
    if request.session.get("id_usuario"):
        listatabla=Cliente.objects.all()
        listadepartamento = Departamento.objects.all()
        listaciudad = Ciudad.objects.all()
        listanacionalidad = Nacionalidad.objects.all()
        return validar(request, "clients/vercliente.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Clientes", "subtitulo_f":"Listado de Clientes registrados", "listatabla":listatabla})
    else:
        return redirect("login")

def modcliente(request, cliente_actual=0):
    print(cliente_actual)
    if request.session.get("id_usuario"):
        if request.method=="GET":
            cli_actual=Cliente.objects.filter(codigo_cliente=cliente_actual).exists()
            
            if cli_actual:
                datos_cliente=Cliente.objects.filter(codigo_cliente=cliente_actual).first()
                return validar(request, "clients/modcliente.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Cliente", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_cliente, 
                "cliente_actual":cliente_actual})
            else:
                return validar(request, "clients/modcliente.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Nuevo Cliente", "subtitulo_f":"Por favor complete todos los datos solicitados", 
                "cliente_actual":cliente_actual})

        if request.method=="POST":
            if cliente_actual==0:
                cliente_nuevo=Cliente(codigo_cliente=request.POST.get('codigo_cliente'),
                nombre_cliente=request.POST.get('nombre_cliente'),
                ruc_cliente=request.POST.get('ruc_cliente'),
                telefono_cliente=request.POST.get('telefono_cliente'),
                direccion_cliente=request.POST.get("direccion_cliente"),
                genero_cliente=request.POST.get("genero_cliente"))

                cliente_nuevo.save()
            else:
                cliente_actual=Cliente.objects.get(codigo_cliente=cliente_actual)
                cliente_actual.nombre_cliente=request.POST.get('nombre_cliente')
                cliente_actual.ruc_cliente=request.POST.get('ruc_cliente')
                cliente_actual.telefono_cliente=request.POST.get('telefono_cliente')
                cliente_actual.direccion_cliente=request.POST.get("direccion_cliente")
                cliente_actual.genero_cliente=request.POST.get("genero_cliente")
                cliente_actual.save() 

        return redirect('vercliente')
    
    else:
        return redirect("login")

def borcliente(request, cliente_actual):
        Cliente.objects.filter(codigo_cliente = cliente_actual).delete()
        return redirect('vercliente')

#--=======================================Proveedor======================================--

def verproveedor(request):
    if request.session.get("id_usuario"):
        listatabla=Proveedor.objects.all()
        return validar(request, "proveedor/verproveedor.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Proveedores", "subtitulo_f":"Listado de Proveedores registrados", "listatabla":listatabla})
    else:
        return redirect("login")

def modproveedor(request,proveedor_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            prov_actual=Proveedor.objects.filter(codigo_proveedor=proveedor_actual).exists()
            if prov_actual:
                datos_proveedor=Proveedor.objects.filter(codigo_proveedor=proveedor_actual).first()
                return validar(request, "proveedor/modproveedor.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Proveedor", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_proveedor, 
                "proveedor_actual":proveedor_actual})
            else:
                return validar(request, "proveedor/modproveedor.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Nuevo Proveedor", "subtitulo_f":"Por favor complete todos los datos solicitados", "proveedor_actual":proveedor_actual})

        if request.method=="POST":
            if proveedor_actual==0:
                proveedor_nuevo=Proveedor(codigo_proveedor=request.POST.get('codigo_proveedor'),
                nombre_proveedor=request.POST.get('nombre_proveedor'),
                razon_social_proveedor=request.POST.get('razon_social_proveedor'),
                ruc_proveedor=request.POST.get('ruc_proveedor'),
                telefono_proveedor=request.POST.get('telefono_proveedor'),
                direccion_proveedor=request.POST.get("direccion_proveedor"))

                proveedor_nuevo.save()
            else:
                proveedor_actual=Proveedor.objects.get(codigo_proveedor=proveedor_actual)
                proveedor_actual.nombre_proveedor=request.POST.get('nombre_proveedor')
                proveedor_actual.razon_social_proveedor=request.POST.get('razon_social_proveedor')
                proveedor_actual.ruc_proveedor=request.POST.get('ruc_proveedor')
                proveedor_actual.telefono_proveedor=request.POST.get('telefono_proveedor')
                proveedor_actual.direccion_proveedor=request.POST.get("direccion_proveedor")
                proveedor_actual.save() 

        return redirect('verproveedor')
    
    else:
        return redirect("login")

def borproveedor(request, proveedor_actual):
        Proveedor.objects.filter(codigo_proveedor = proveedor_actual).delete()
        return redirect('verproveedor')

#--=======================================Departamentos======================================--

def verdepartamento(request):
    if request.session.get("id_usuario"):
        listatabla = Departamento.objects.all()
        return validar(request, "departamentos/verdepartamento.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Departamentos", "subtitulo_f":"Listado de Departamentos registrados", "listatabla":listatabla})
    else:
        return redirect("login")

def moddepartamento(request,departamento_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            dept_actual=Departamento.objects.filter(codigo_departamento=departamento_actual).exists()
            if dept_actual:
                datos_departamento=Departamento.objects.filter(codigo_departamento=departamento_actual).first()
                return validar(request, "departamentos/moddepartamento.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Departamento", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_departamento, 
                "departamento_actual":departamento_actual})
            else:
                return validar(request, "departamentos/moddepartamento.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Nuevo Proveedor", "subtitulo_f":"Por favor complete todos los datos solicitados", "departamento_actual":departamento_actual})

        if request.method=="POST":
            if departamento_actual==0:
                departamento_nuevo=Departamento(codigo_departamento=request.POST.get('codigo_departamento'),
                nombre_departamento=request.POST.get('nombre_departamento'))
                departamento_nuevo.save()

            else:
                departamento_actual=Departamento.objects.get(codigo_departamento=departamento_actual)
                departamento_actual.nombre_departamento=request.POST.get('nombre_departamento')
                departamento_actual.save() 

        return redirect('verdepartamento')
    
    else:
        return redirect("login")

def bordepartamento(request, departamento_actual):
        Departamento.objects.filter(codigo_departamento = departamento_actual).delete()
        return redirect('verdepartamento')

#--=======================================Ciudades======================================--

def verciudad(request):
    if request.session.get("id_usuario"):
        listatabla = Ciudad.objects.all()
        listadepartamento = Departamento.objects.all()
        return validar(request, "ciudad/verciudad.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Ciudades", "subtitulo_f":"Listado de Ciudades registrados", "listatabla":listatabla, "listadepartamento": listadepartamento})
    else:
        return redirect("login")

def modciudad(request,ciudad_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            listadepartamento = Departamento.objects.all()
            ciu_actual=Ciudad.objects.filter(codigo_ciudad=ciudad_actual).exists()
            if ciu_actual:
                datos_ciudad=Ciudad.objects.filter(codigo_ciudad=ciudad_actual).first()
                return validar(request, "ciudad/modciudad.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Ciudad", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_ciudad, 
                "ciudad_actual":ciudad_actual})
            else:
                return validar(request, "ciudad/modciudad.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Nueva Ciudad", "subtitulo_f":"Por favor complete todos los datos solicitados", 
                "ciudad_actual":ciudad_actual, 
                "listadepartamento":listadepartamento})

        if request.method=="POST":
            if ciudad_actual==0:
                ciudad_nuevo=Ciudad(codigo_ciudad=request.POST.get('codigo_ciudad'),
                nombre_ciudad=request.POST.get('nombre_ciudad'),
                nombre_departamento_id=request.POST.get('departamento'))
                ciudad_nuevo.save()
                listadepartamento = Departamento.objects.all()

            else:
                ciudad_actual=Ciudad.objects.get(codigo_ciudad=ciudad_actual)
                listadepartamento = Departamento.objects.all()
                ciudad_actual.nombre_ciudad=request.POST.get('nombre_ciudad')
                ciudad_actual.nombre_departamento_id=request.get("departamento")
                ciudad_actual.save() 

        return redirect('verciudad')
    
    else:
        return redirect("login")

def borciudad(request, ciudad_actual):
        Ciudad.objects.filter(codigo_ciudad = ciudad_actual).delete()
        return redirect('verciudad')

#--=======================================Productos======================================--
def cpu(request):
    return validar(request, "productos/cpu.html")

def case(request):
    return validar(request, "productos/case.html")
    
def motherboard(request):
    return validar(request, "productos/motherboard.html")

def perifericos(request):
    return validar(request, "productos/perifericos.html")

def psu(request):
    return validar(request, "productos/psu.html")

def ram(request):
    return validar(request, "productos/ram.html")

def stg(request):
    return validar(request, "productos/stg.html")

def vga(request):
    return validar(request, "productos/vga.html")

 
#--=======================================Validación======================================--
def validar(request, pageSuccess, parameters={}):
    if request.session.get("id_usuario"):
        if (request.session.get("tipo_usuario") == 2) and ((pageSuccess == 'users.html') or (pageSuccess == 'products.html')):
            return render(request, "index.html", {"nombre_usuario": request.session.get("nombre_completo_usuario"),"tipo_usuario": request.session.get("tipo_usuario"), "mensaje": "Este usuario no cuenta con los privilegios suficientes"})
        else: 
            return render(request, pageSuccess, {"nombre_usuario": request.session.get("nombre_completo_usuario"),"tipo_usuario": request.session.get("tipo_usuario"), "parameters": parameters})
    else:
        return render(request, 'login.html')



