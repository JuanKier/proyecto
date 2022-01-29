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

def produccion(request):
    return validar(request, "produccion.html")

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
        return validar(request, "clients/vercliente.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Clientes", "subtitulo_f":"Listado de Clientes registrados", 
        "listatabla":listatabla, 
        "listadepartamento": listadepartamento,
        "listaciudad": listaciudad,
        "listanacionalidad": listanacionalidad})
    else:
        return redirect("login")

def modcliente(request, cliente_actual=0):
    print(cliente_actual)
    if request.session.get("id_usuario"):
        if request.method=="GET":
            listadepartamento = Departamento.objects.all()
            listaciudad = Ciudad.objects.all()
            listanacionalidad = Nacionalidad.objects.all()
            cli_actual=Cliente.objects.filter(codigo_cliente=cliente_actual).exists()
            if cli_actual:
                datos_cliente=Cliente.objects.filter(codigo_cliente=cliente_actual).first()
                return validar(request, "clients/modcliente.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Cliente", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_cliente, 
                "cliente_actual":cliente_actual,
                "listadepartamento": listadepartamento,
                "listaciudad": listaciudad,
                "listanacionalidad": listanacionalidad})
            else:
                return validar(request, "clients/modcliente.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Nuevo Cliente", "subtitulo_f":"Por favor complete todos los datos solicitados", 
                "cliente_actual":cliente_actual,
                "listadepartamento": listadepartamento,
                "listaciudad": listaciudad,
                "listanacionalidad": listanacionalidad})

        if request.method=="POST":
            if cliente_actual==0:
                cliente_nuevo=Cliente(codigo_cliente=request.POST.get('codigo_cliente'),
                nombre_cliente=request.POST.get('nombre_cliente'),
                ruc_cliente=request.POST.get('ruc_cliente'),
                telefono_cliente=request.POST.get('telefono_cliente'),
                direccion_cliente=request.POST.get("direccion_cliente"),
                genero_cliente=request.POST.get("genero_cliente"),
                nombre_departamento_id=request.POST.get('departamento'),
                nombre_ciudad_id=request.POST.get('ciudad'),
                descripcion_nacionalidad_id=request.POST.get('nacionalidad'))

                cliente_nuevo.save()
            else:
                cliente_actual=Cliente.objects.get(codigo_cliente=cliente_actual)
                cliente_actual.nombre_cliente=request.POST.get('nombre_cliente')
                cliente_actual.ruc_cliente=request.POST.get('ruc_cliente')
                cliente_actual.telefono_cliente=request.POST.get('telefono_cliente')
                cliente_actual.direccion_cliente=request.POST.get('direccion_cliente')
                cliente_actual.genero_cliente=request.POST.get('genero_cliente')
                cliente_actual.nombre_departamento_id = request.POST.get('departamento')
                cliente_actual.nombre_ciudad_id = request.POST.get('ciudad')
                cliente_actual.descripcion_nacionalidad_id = request.POST.get('nacionalidad')
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


def modciudad(request, ciudad_actual=0):
    if request.session.get("id_usuario"):
        if request.method == "GET":
            listadepartamento = Departamento.objects.all()
            ciu_actual = Ciudad.objects.filter(
                codigo_ciudad=ciudad_actual).exists()
            if ciu_actual:
                datos_ciudad = Ciudad.objects.filter(
                    codigo_ciudad=ciudad_actual).first()
                return validar(request, "ciudad/modciudad.html",
                               {"nombre_completo_usuario": request.session.get("nombre_completo_usuario"),
                                "titulo_f": "Modificar Ciudad",
                                "subtitulo_f": "Vuelva a escribir los datos que desea modificar",
                                "datos_act": datos_ciudad,
                                "ciudad_actual": ciudad_actual,
                                "listadepartamento": listadepartamento})
            else:
                return validar(request, "ciudad/modciudad.html", {"nombre_completo_usuario": request.session.get("nombre_completo_usuario"),
                                                                  "titulo_f": "Nueva Ciudad", "subtitulo_f": "Por favor complete todos los datos solicitados",
                                                                  "ciudad_actual": ciudad_actual,
                                                                  "listadepartamento": listadepartamento})

        if request.method == "POST":
            if ciudad_actual == 0:
                ciudad_nuevo = Ciudad(codigo_ciudad=request.POST.get('codigo_ciudad'),
                                      nombre_ciudad=request.POST.get('nombre_ciudad'),
                                      nombre_departamento_id=request.POST.get('departamento'))
                ciudad_nuevo.save()

            else:
                ciudad_actual = Ciudad.objects.get(codigo_ciudad=ciudad_actual)
                ciudad_actual.nombre_ciudad = request.POST.get('nombre_ciudad')
                ciudad_actual.nombre_departamento_id = request.get('departamento')
                ciudad_actual.save()
                

        return redirect('verciudad')

    else:
        return redirect("login")

def borciudad(request, ciudad_actual):
        Ciudad.objects.filter(codigo_ciudad = ciudad_actual).delete()
        return redirect('verciudad')

#--=======================================Nacionalidades======================================--


def vernacionalidad(request):
    if request.session.get("id_usuario"):
        listatabla = Nacionalidad.objects.all()
        return validar(request, "nacionalidades/vernacionalidad.html", 
        {"nombre_completo_usuario": request.session.get("nombre_completo_usuario"), 
        "titulo_f": "Nacionalidades", "subtitulo_f": "Listado de Nacionalidades registrados", 
        "listatabla": listatabla})
    else:
        return redirect("login")


def modnacionalidad(request, nacionalidad_actual=0):
    if request.session.get("id_usuario"):
        if request.method == "GET":
            dept_actual = Nacionalidad.objects.filter(
                codigo_nacionalidad=nacionalidad_actual).exists()
            if dept_actual:
                datos_nacionalidad = Nacionalidad.objects.filter(
                    codigo_nacionalidad=nacionalidad_actual).first()
                return validar(request, "nacionalidades/modnacionalidad.html",
                               {"nombre_completo_usuario": request.session.get("nombre_completo_usuario"),
                                "titulo_f": "Modificar Nacionalidad",
                                "subtitulo_f": "Vuelva a escribir los datos que desea modificar",
                                "datos_act": datos_nacionalidad,
                                "nacionalidad_actual": nacionalidad_actual})
            else:
                return validar(request, "nacionalidades/modnacionalidad.html", 
                {"nombre_completo_usuario": request.session.get("nombre_completo_usuario"), 
                "titulo_f": "Nuevo Proveedor", 
                "subtitulo_f": "Por favor complete todos los datos solicitados", 
                "nacionalidad_actual": nacionalidad_actual})

        if request.method == "POST":
            if nacionalidad_actual == 0:
                nacionalidad_nuevo = Nacionalidad(codigo_nacionalidad=request.POST.get('codigo_nacionalidad'),
                                                  descripcion_nacionalidad=request.POST.get('descripcion_nacionalidad'))
                nacionalidad_nuevo.save()

            else:
                nacionalidad_actual = Nacionalidad.objects.get(
                    codigo_nacionalidad=nacionalidad_actual)
                nacionalidad_actual.descripcion_nacionalidad = request.POST.get('descripcion_nacionalidad')
                nacionalidad_actual.save()

        return redirect('vernacionalidad')

    else:
        return redirect("login")


def bornacionalidad(request, nacionalidad_actual):
    Nacionalidad.objects.filter(
        codigo_nacionalidad=nacionalidad_actual).delete()
    return redirect('vernacionalidad')


#--=======================================Mantenimiento======================================--

def vermant(request):
    if request.session.get("id_usuario"):
        listatabla=Mantenimiento.objects.all()
        listacliente=Cliente.objects.all()
        listausuario = Usuario.objects.all()
        return validar(request, "produccion/vermant.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Mantenimientos", "subtitulo_f":"Listado de Mantenimientos registrados", 
        "listatabla":listatabla, 
        "listacliente": listacliente,
        "listausuario": listausuario})
    else:
        return redirect("login")

def modmant(request, mant_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            listacliente=Cliente.objects.all()
            listausuario = Usuario.objects.all()
            mante_actual=Mantenimiento.objects.filter(codigo_mant=mant_actual).exists()
            if mante_actual:
                datos_mant=Mantenimiento.objects.filter(codigo_mant=mant_actual).first()
                return validar(request, "produccion/modmant.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Mantenimiento", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_mant, 
                "mant_actual":mant_actual,
                "listacliente": listacliente,
                "listausuario": listausuario})
            else:
                return validar(request, "produccion/modmant.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Nuevo Cliente", "subtitulo_f":"Por favor complete todos los datos solicitados", 
                "mant_actual":mant_actual,
                "listacliente": listacliente,
                "listausuario": listausuario})

        if request.method=="POST":
            if mant_actual==0:
                mant_nuevo=Mantenimiento(codigo_mant=request.POST.get('codigo_mant'),
                equipo_mant=request.POST.get('equipo_mant'),
                desc_equipo_mant=request.POST.get('desc_equipo_mant'),
                horas_mant=request.POST.get("horas_mant"),
                actividades_mant=request.POST.get("actividades_mant"),
                inicio_mant=request.POST.get('inicio_mant'),
                fin_mant=request.POST.get("fin_mant"),
                nombre_cliente_id=request.POST.get('cliente'),
                nombre_completo_usuario_id=request.POST.get('empleado'))

                mant_nuevo.save()
            else:
                mant_actual=Mantenimiento.objects.get(codigo_mant=mant_actual)
                mant_actual.equipo_mant=request.POST.get('equipo_mant')
                mant_actual.desc_equipo_mant=request.POST.get('desc_equipo_mant')
                mant_actual.horas_mant=request.POST.get('horas_mant')
                mant_actual.actividades_mant=request.POST.get('actividades_mant')
                mant_actual.inicio_mant=request.POST.get('inicio_mant')
                mant_actual.fin_mant=request.POST.get('fin_mant')
                mant_actual.nombre_cliente_id = request.POST.get('cliente')
                mant_actual.nombre_completo_usuario_id = request.POST.get('empleado')

                mant_actual.save() 

        return redirect('vermant')
    
    else:
        return redirect("login")

def bormant(request, mant_actual):
        Cliente.objects.filter(codigo_mant = mant_actual).delete()
        return redirect('vermant')



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
        if (request.session.get("tipo_usuario") == 2) and ((pageSuccess == 'users/verusuario.html') or (pageSuccess == 'products.html') or (pageSuccess == 'profile.html')):
            return render(request, "index.html", {"nombre_usuario": request.session.get("nombre_completo_usuario"),"tipo_usuario": request.session.get("tipo_usuario"), "mensaje": "Este usuario no cuenta con los privilegios suficientes"})
        else: 
            return render(request, pageSuccess, {"nombre_usuario": request.session.get("nombre_completo_usuario"),"tipo_usuario": request.session.get("tipo_usuario"), "parameters": parameters})
    else:
        return render(request, 'login.html')



