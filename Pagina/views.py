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
    if request.session.get("id_usuario"):
        listatabla=Placa_base.objects.all()
        listagabinete = Tipo_Gabinete.objects.all()
        listaproveedor = Proveedor.objects.all()
        return validar(request, "index.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Usuarios", "subtitulo_f":"Listado de Usuarios registrados", "listatabla":listatabla, "listagabinete":listagabinete,"listaproveedor": listaproveedor})
    else:
        return redirect("login")
     
def venta(request):
    if request.session.get("id_usuario"):
        listaperiferico = Perifericos.objects.all()
        listagabinete = Gabinete.objects.all()
        listacpu = CPU.objects.all()
        listaram = RAM.objects.all()
        listaplaca = Placa_base.objects.all()
        listarepuesto = Repuestos.objects.all()
        listaproveedor = Proveedor.objects.all()
        listacliente = Cliente.objects.all()
        return validar(request, "venta.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Nueva Venta", 
        "listagabinete":listagabinete,
        "listaperiferico":listaperiferico,
        "listacpu":listacpu,
        "listaram":listaram,
        "listaplaca":listaplaca,
        "listaproveedor":listaproveedor,
        "listacliente":listacliente,
        "listarepuesto": listarepuesto})
    else:
        return redirect("login")  

def salir(request):
    request.session.flush()
    return redirect("./") 

def inventario(request):
    return validar(request, "inventario.html")

def produccion(request):
    if request.session.get("id_usuario"):
        listatabla=Placa_base.objects.all()
        listagabinete = Tipo_Gabinete.objects.all()
        listaproveedor = Proveedor.objects.all()
        return validar(request, "produccion.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Usuarios", "subtitulo_f":"Listado de Usuarios registrados", "listatabla":listatabla, "listagabinete":listagabinete,"listaproveedor": listaproveedor})
    else:
        return redirect("login")

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

#--=======================================Maintenance======================================--
#--=======================================Departamentos======================================--

def verdepartamento(request):
    if request.session.get("id_usuario"):
        listatabla = Departamento.objects.all()
        return validar(request, "maintenance/departamentos/verdepartamento.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Departamentos", "subtitulo_f":"Listado de Departamentos registrados", "listatabla":listatabla})
    else:
        return redirect("login")

def moddepartamento(request,departamento_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            dept_actual=Departamento.objects.filter(codigo_departamento=departamento_actual).exists()
            if dept_actual:
                datos_departamento=Departamento.objects.filter(codigo_departamento=departamento_actual).first()
                return validar(request, "maintenance/departamentos/moddepartamento.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Departamento", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_departamento, 
                "departamento_actual":departamento_actual})
            else:
                return validar(request, "maintenance/departamentos/moddepartamento.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Nuevo Departamento", "subtitulo_f":"Por favor complete todos los datos solicitados", "departamento_actual":departamento_actual})

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
        return validar(request, "maintenance/ciudad/verciudad.html", {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), "titulo_f":"Ciudades", "subtitulo_f":"Listado de Ciudades registrados", "listatabla":listatabla, "listadepartamento": listadepartamento})
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
                return validar(request, "maintenance/ciudad/modciudad.html",
                               {"nombre_completo_usuario": request.session.get("nombre_completo_usuario"),
                                "titulo_f": "Modificar Ciudad",
                                "subtitulo_f": "Vuelva a escribir los datos que desea modificar",
                                "datos_act": datos_ciudad,
                                "ciudad_actual": ciudad_actual,
                                "listadepartamento": listadepartamento})
            else:
                return validar(request, "maintenance/ciudad/modciudad.html", {"nombre_completo_usuario": request.session.get("nombre_completo_usuario"),
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
        return validar(request, "maintenance/nacionalidades/vernacionalidad.html", 
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
                return validar(request, "maintenance/nacionalidades/modnacionalidad.html",
                               {"nombre_completo_usuario": request.session.get("nombre_completo_usuario"),
                                "titulo_f": "Modificar Nacionalidad",
                                "subtitulo_f": "Vuelva a escribir los datos que desea modificar",
                                "datos_act": datos_nacionalidad,
                                "nacionalidad_actual": nacionalidad_actual})
            else:
                return validar(request, "maintenance/nacionalidades/modnacionalidad.html", 
                {"nombre_completo_usuario": request.session.get("nombre_completo_usuario"), 
                "titulo_f": "Nueva Nacionalidad", 
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

#--=======================================Tipos_Ram======================================--

def vertipo_ram(request):
    if request.session.get("id_usuario"):
        listatabla = Tipo_Ram.objects.all()
        return validar(request, "maintenance/tipo_ram/vertipo_ram.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Tipos de Ram", 
        "subtitulo_f":"Listado de Tipos de Ram registrados", 
        "listatabla":listatabla})
    else:
        return redirect("login")

def modtipo_ram(request,tipo_ram_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            ram_actual=Tipo_Ram.objects.filter(id_tipo_ram=tipo_ram_actual).exists()
            if ram_actual:
                datos_tipo_ram=Tipo_Ram.objects.filter(id_tipo_ram=tipo_ram_actual).first()
                return validar(request, "maintenance/tipo_ram/modtipo_ram.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Tipo Ram", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_tipo_ram, 
                "tipo_ram_actual":tipo_ram_actual})
            else:
                return validar(request, "maintenance/tipo_ram/modtipo_ram.html", { 
                    "nombre_completo_usuario": request.session.get("nombre_completo_usuario"), 
                    "titulo_f": "Nuevo Tipo de Ram", 
                    "subtitulo_f": "Por favor complete todos los datos solicitados", 
                    "tipo_ram_actual": tipo_ram_actual})

        if request.method=="POST":
            if tipo_ram_actual==0:
                tipo_ram_nuevo=Tipo_Ram(desc_tipo_ram=request.POST.get('desc_tipo_ram'))
                tipo_ram_nuevo.save()

            else:
                tipo_ram_actual=Tipo_Ram.objects.get(id_tipo_ram=tipo_ram_actual)
                tipo_ram_actual.desc_tipo_ram=request.POST.get('desc_tipo_ram')
                tipo_ram_actual.save() 

        return redirect('vertipo_ram')
    
    else:
        return redirect("login")

def bortipo_ram(request, tipo_ram_actual):
        Tipo_Ram.objects.filter(id_tipo_ram = tipo_ram_actual).delete()
        return redirect('vertipo_ram')

#--=======================================Tipos_CPU======================================--

def vertipo_cpu(request):
    if request.session.get("id_usuario"):
        listatabla = Tipo_Cpu.objects.all()
        return validar(request, "maintenance/tipo_cpu/vertipo_cpu.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Tipos de CPU", 
        "subtitulo_f":"Listado de Tipos de CPU registrados", 
        "listatabla":listatabla})
    else:
        return redirect("login")

def modtipo_cpu(request,tipo_cpu_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            cpu_actual=Tipo_Cpu.objects.filter(id_tipo_cpu=tipo_cpu_actual).exists()
            if cpu_actual:
                datos_tipo_cpu=Tipo_Cpu.objects.filter(id_tipo_cpu=tipo_cpu_actual).first()
                return validar(request, "maintenance/tipo_cpu/modtipo_cpu.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Tipo CPU", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_tipo_cpu, 
                "tipo_cpu_actual":tipo_cpu_actual})
            else:
                return validar(request, "maintenance/tipo_cpu/modtipo_cpu.html", { 
                    "nombre_completo_usuario": request.session.get("nombre_completo_usuario"), 
                    "titulo_f": "Nuevo Tipo de CPU", 
                    "subtitulo_f": "Por favor complete todos los datos solicitados", 
                    "tipo_cpu_actual": tipo_cpu_actual})

        if request.method=="POST":
            if tipo_cpu_actual==0:
                tipo_cpu_nuevo=Tipo_Cpu(desc_tipo_cpu=request.POST.get('desc_tipo_cpu'))
                tipo_cpu_nuevo.save()

            else:
                tipo_cpu_actual=Tipo_Cpu.objects.get(id_tipo_cpu=tipo_cpu_actual)
                tipo_cpu_actual.desc_tipo_cpu=request.POST.get('desc_tipo_cpu')
                tipo_cpu_actual.save() 

        return redirect('vertipo_cpu')
    
    else:
        return redirect("login")

def bortipo_cpu(request, tipo_cpu_actual):
        Tipo_Cpu.objects.filter(id_tipo_cpu = tipo_cpu_actual).delete()
        return redirect('vertipo_cpu')

#--=======================================Tipos_CPU======================================--

def vertipo_gabinete(request):
    if request.session.get("id_usuario"):
        listatabla = Tipo_Gabinete.objects.all()
        return validar(request, "maintenance/tipo_gabinete/vertipo_gabinete.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Tipos de Gabinete", 
        "subtitulo_f":"Listado de Tipos de Gabinetes registrados", 
        "listatabla":listatabla})
    else:
        return redirect("login")

def modtipo_gabinete(request,tipo_gabinete_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            cpu_actual=Tipo_Gabinete.objects.filter(id_tipo_gabinete=tipo_gabinete_actual).exists()
            if cpu_actual:
                datos_tipo_gabinete=Tipo_Gabinete.objects.filter(id_tipo_gabinete=tipo_gabinete_actual).first()
                return validar(request, "maintenance/tipo_gabinete/modtipo_gabinete.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Tipo de Gabinete", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_tipo_gabinete, 
                "tipo_gabinete_actual":tipo_gabinete_actual})
            else:
                return validar(request, "maintenance/tipo_gabinete/modtipo_gabinete.html", { 
                    "nombre_completo_usuario": request.session.get("nombre_completo_usuario"), 
                    "titulo_f": "Nuevo Tipo de CPU", 
                    "subtitulo_f": "Por favor complete todos los datos solicitados", 
                    "tipo_gabinete_actual": tipo_gabinete_actual})

        if request.method=="POST":
            if tipo_gabinete_actual==0:
                tipo_gabinete_nuevo=Tipo_Gabinete(desc_tipo_gabinete=request.POST.get('desc_tipo_gabinete'))
                tipo_gabinete_nuevo.save()

            else:
                tipo_gabinete_actual=Tipo_Gabinete.objects.get(id_tipo_gabinete=tipo_gabinete_actual)
                tipo_gabinete_actual.desc_tipo_gabinete=request.POST.get('desc_tipo_gabinete')
                tipo_gabinete_actual.save() 

        return redirect('vertipo_gabinete')
    
    else:
        return redirect("login")

def bortipo_gabinete(request, tipo_cpu_actual):
        Tipo_Gabinete.objects.filter(id_tipo_cpu = tipo_cpu_actual).delete()
        return redirect('vertipo_gabinete')

#--=========================================SERVICIOS========================================--
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
                datos_mant.inicio_mant=str(datos_mant.inicio_mant)
                datos_mant.fin_mant=str(datos_mant.fin_mant)
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
                "titulo_f":"Nuevo Mantenimiento", "subtitulo_f":"Por favor complete todos los datos solicitados", 
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
                fin_mant=request.POST.get('fin_mant'),
                estado_mant=request.POST.get('estado_mant'),
                nombre_cliente_id=request.POST.get('id_cliente'),
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
                mant_actual.estado_mant=request.POST.get('estado_mant')
                mant_actual.nombre_cliente_id = request.POST.get('id_cliente')
                mant_actual.nombre_completo_usuario_id = request.POST.get('empleado')

                mant_actual.save() 

        return redirect('vermant')
    
    else:
        return redirect("login")

def bormant(request, mant_actual):
        Mantenimiento.objects.filter(codigo_mant = mant_actual).delete()
        return redirect('vermant')

#--=======================================Reparacion======================================--

def verrep(request):
    if request.session.get("id_usuario"):
        listatabla=Reparacion.objects.all()
        listacliente=Cliente.objects.all()
        listausuario = Usuario.objects.all()
        return validar(request, "produccion/verrep.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Reparaciones", "subtitulo_f":"Listado de Reparaciones registradas", 
        "listatabla":listatabla, 
        "listacliente": listacliente,
        "listausuario": listausuario})
    else:
        return redirect("login")

def modrep(request, rep_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            listacliente=Cliente.objects.all()
            listausuario = Usuario.objects.all()
            repa_actual=Reparacion.objects.filter(codigo_rep=rep_actual).exists()
            if repa_actual:
                datos_rep=Reparacion.objects.filter(codigo_rep=rep_actual).first()
                datos_rep.inicio_rep=str(datos_rep.inicio_rep)
                datos_rep.fin_rep=str(datos_rep.fin_rep)
                return validar(request, "produccion/modrep.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Reparación", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_rep, 
                "rep_actual":rep_actual,
                "listacliente": listacliente,
                "listausuario": listausuario})
            else:
                return validar(request, "produccion/modrep.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Nueva Reparacion", "subtitulo_f":"Por favor complete todos los datos solicitados", 
                "rep_actual":rep_actual,
                "listacliente": listacliente,
                "listausuario": listausuario})

        if request.method=="POST":
            if rep_actual==0:
                rep_nuevo=Reparacion(codigo_rep=request.POST.get('codigo_rep'),
                equipo_rep=request.POST.get('equipo_rep'),
                desc_equipo_rep=request.POST.get('desc_equipo_rep'),
                horas_rep=request.POST.get("horas_rep"),
                actividades_rep=request.POST.get("actividades_rep"),
                inicio_rep=request.POST.get('inicio_rep'),
                fin_rep=request.POST.get('fin_rep'),
                estado_rep=request.POST.get('estado_rep'),
                nombre_cliente_id=request.POST.get('id_cliente'),
                nombre_completo_usuario_id=request.POST.get('empleado'))

                rep_nuevo.save()
            else:
                rep_actual=Reparacion.objects.get(codigo_rep=rep_actual)
                rep_actual.equipo_rep=request.POST.get('equipo_rep')
                rep_actual.desc_equipo_rep=request.POST.get('desc_equipo_rep')
                rep_actual.horas_rep=request.POST.get('horas_rep')
                rep_actual.actividades_rep=request.POST.get('actividades_rep')
                rep_actual.inicio_rep=request.POST.get('inicio_rep')
                rep_actual.fin_rep=request.POST.get('fin_rep')
                rep_actual.estado_rep=request.POST.get('estado_rep')
                rep_actual.nombre_cliente_id = request.POST.get('id_cliente')
                rep_actual.nombre_completo_usuario_id = request.POST.get('empleado')

                rep_actual.save() 

        return redirect('verrep')
    
    else:
        return redirect("login")

def borrep(request, rep_actual):
        Reparacion.objects.filter(codigo_rep = rep_actual).delete()
        return redirect('verrep')

#--=======================================Montaje======================================--

def vermontaje(request):
    if request.session.get("id_usuario"):
        listaplaca=Placa_base.objects.all()
        listaram = RAM.objects.all()
        listacpu = CPU.objects.all()
        listagabinete = Gabinete.objects.all()
        listaperiferico = Perifericos.objects.all()
        listausuario = Usuario.objects.all()
        listacliente = Cliente.objects.all()
        listatabla = Montaje.objects.all()
        listamontaje=Montaje.objects.all()
        return validar(request, "produccion/vermontaje.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Reparaciones", "subtitulo_f":"Listado de Reparaciones registradas", 
        "listatabla":listatabla, 
        "listaram": listaram,
        "listacpu": listacpu,
        "listagabinete": listagabinete,
        "listaplaca":listaplaca,
        "listacliente": listacliente,
        "listaperiferico":listaperiferico,
        "listamontaje":listamontaje,
        "listausuario": listausuario})
    else:
        return redirect("login")

def nuevomontaje (request, placa_base_actual, montaje_actual=0):
    if request.session.get("id_usuario"):
        if request.method == "GET":
            listamontaje=Montaje.objects.all()
            datosplaca=Placa_base.objects.get(id_placa_base=placa_base_actual)
            tipo_ram_placa = datosplaca.tipo_ram_placa_base_id
            tipo_cpu_placa = datosplaca.tipo_cpu_placa_base_id
            tipo_gabinete_placa = datosplaca.tipo_gabinete_placa_base_id
            listaram = RAM.objects.filter(tipo_ram_id=tipo_ram_placa)
            listacpu = CPU.objects.filter(tipo_cpu_id=tipo_cpu_placa)
            listagabinete = Gabinete.objects.filter(tipo_gabinete_id=tipo_gabinete_placa)
            listaperiferico = Perifericos.objects.all()
            listausuario = Usuario.objects.all()
            listacliente = Cliente.objects.all()
            mont_actual=Montaje.objects.filter(codigo_montaje=montaje_actual).exists()
            if mont_actual:
                datos_mont=Montaje.objects.filter(codigo_montaje=montaje_actual).first()
                datos_mont.inicio_mont=str(datos_mont.inicio_mont)
                datos_mont.fin_mont=str(datos_mont.fin_mont)
                return validar(request, "produccion/nuevomontaje.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Montaje", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_mont, 
                "montaje_actual":montaje_actual,
                "placa_base_actual":placa_base_actual, 
                "listaram": listaram,
                "listacpu": listacpu,
                "listagabinete": listagabinete,
                "datosplaca":datosplaca,
                "listacliente": listacliente,
                "listaperiferico":listaperiferico,
                "listamontaje":listamontaje,
                "listausuario": listausuario})
            else:
                return validar(request, "produccion/nuevomontaje.html", 
                        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                        "titulo_f":"Nuevo Montaje", 
                        "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                        "montaje_actual":montaje_actual,
                        "placa_base_actual":placa_base_actual, 
                        "listamontaje":listamontaje,
                        "listaram": listaram,
                        "listacpu": listacpu,
                        "listagabinete": listagabinete,
                        "datosplaca":datosplaca,
                        "listausuario":listausuario,
                        "listacliente":listacliente,
                        "listaperiferico":listaperiferico})

        if request.method=="POST":
            print(request.POST.get('placa_base_actual'))
            if montaje_actual==0:
                montaje_nuevo=Montaje(codigo_montaje=request.POST.get('codigo_montaje'),
                id_placa_base_id=request.POST.get('placa_base_actual'),
                tipo_gabinete_id=request.POST.get('tipo_gabinete'),
                tipo_ram_id=request.POST.get('tipo_ram'),
                tipo_cpu_id=request.POST.get('tipo_cpu'),
                id_periferico_id=request.POST.get('tipo_periferico'),
                nombre_cliente_id=request.POST.get('id_cliente'),
                horas_mont=request.POST.get('horas_mont'),
                inicio_mont=request.POST.get('inicio_mont'),
                fin_mont=request.POST.get('fin_mont'),
                estado_mont=request.POST.get('estado_mont'),
                actividades_mont=request.POST.get('actividades_mont'),
                tipo_placa_video=request.POST.get('tipo_placa_video'),
                tipo_fuente=request.POST.get('tipo_fuente'),
                tipo_almacenamiento=request.POST.get('tipo_almacenamiento'),
                nombre_completo_usuario_id=request.POST.get('empleado'))

                montaje_nuevo.save()
            else:
                montaje_actual=Montaje.objects.get(codigo_montaje=montaje_actual)
                montaje_actual.id_placa_base_id=request.POST.get('placa_base_actual')
                montaje_actual.tipo_gabinete_id=request.POST.get('tipo_gabinete')
                montaje_actual.tipo_ram_id=request.POST.get('tipo_ram')
                montaje_actual.tipo_cpu_id=request.POST.get('tipo_cpu')
                montaje_actual.id_periferico_id=request.POST.get('tipo_periferico')
                montaje_actual.nombre_cliente_id=request.POST.get('id_cliente')
                montaje_actual.horas_mont=request.POST.get('horas_mont')
                montaje_actual.inicio_mont=request.POST.get('inicio_mont')
                montaje_actual.fin_mont=request.POST.get('fin_mont')
                montaje_actual.estado_mont=request.POST.get('estado_mont')
                montaje_actual.actividades_mont=request.POST.get('actividades_mont')
                montaje_actual.nombre_completo_usuario_id=request.POST.get('empleado')
                montaje_actual.tipo_placa_video=request.POST.get('tipo_placa_video')
                montaje_actual.tipo_fuente=request.POST.get('tipo_fuente')
                montaje_actual.tipo_almacenamiento=request.POST.get('tipo_almacenamiento')

                montaje_actual.save() 

        return redirect('vermontaje')
    
    else:
        return redirect("login")

def bormontaje(request, montaje_actual):
        Montaje.objects.filter(codigo_montaje = montaje_actual).delete()
        return redirect('vermontaje')
#--========================================PRODUCTOS======================================--
#--========================================Repuestos======================================--

def repuestover(request):
    if request.session.get("id_usuario"):
        listatabla=Repuestos.objects.all()
        listaproveedor = Proveedor.objects.all()
        return validar(request, "productos/repuestover.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Repuestos", "subtitulo_f":"Listado de Repuestos registrados", 
        "listatabla":listatabla, 
        "listaproveedor": listaproveedor})
    else:
        return redirect("login")

def repuestomod(request, repuesto_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            listaproveedor = Proveedor.objects.all()
            repu_actual=Repuestos.objects.filter(id_repuesto=repuesto_actual).exists()
            if repu_actual:
                datos_repuesto=Repuestos.objects.filter(id_repuesto=repuesto_actual).first()
                return validar(request, "productos/repuestomod.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Reparación", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_repuesto, 
                "repuesto_actual":repuesto_actual,
                "listaproveedor": listaproveedor})
            else:
                return validar(request, "productos/repuestomod.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Nuevo Repuesto", "subtitulo_f":"Por favor complete todos los datos solicitados", 
                "repuesto_actual":repuesto_actual,
                "listaproveedor": listaproveedor})

        if request.method=="POST":
            if repuesto_actual==0:
                repuesto_nuevo=Repuestos(id_repuesto=request.POST.get('id_repuesto'),
                cod_repuesto=request.POST.get('cod_repuesto'),
                tipo_repuesto=request.POST.get('tipo_repuesto'),
                marca_repuesto=request.POST.get('marca_repuesto'),
                descripcion_repuesto=request.POST.get("descripcion_repuesto"),
                nombre_proveedor_id=request.POST.get('proveedor'),
                precio_compra_repuesto=request.POST.get('precio_compra_repuesto'),
                precio_venta_repuesto=request.POST.get('precio_venta_repuesto'),
                imagen_repuesto=request.FILES.get('imagen_repuesto'),
                stock_repuesto=request.POST.get('stock_repuesto'))

                repuesto_nuevo.save()
            else:
                repuesto_actual=Repuestos.objects.get(id_repuesto=repuesto_actual)
                repuesto_actual.cod_repuesto=request.POST.get('cod_repuesto')
                repuesto_actual.tipo_repuesto=request.POST.get('tipo_repuesto')
                repuesto_actual.marca_repuesto=request.POST.get('marca_repuesto')
                repuesto_actual.descripcion_repuesto=request.POST.get('descripcion_repuesto')
                repuesto_actual.nombre_proveedor_id=request.POST.get('proveedor')
                repuesto_actual.precio_compra_repuesto=request.POST.get('precio_compra_repuesto')
                repuesto_actual.precio_venta_repuesto=request.POST.get('precio_venta_repuesto')
                if request.POST.get('imagen_repuesto') != "":
                    repuesto_actual.imagen_repuesto=request.FILES.get('imagen_repuesto')
                else: 
                    repuesto_actual.imagen_repuesto = repuesto_actual.imagen_repuesto
                repuesto_actual.stock_repuesto = request.POST.get('stock_repuesto')

                repuesto_actual.save() 

        return redirect('repuestover')
    
    else:
        return redirect("login")

def repuestobor(request, repuesto_actual):
        Repuestos.objects.filter(id_repuesto = repuesto_actual).delete()
        return redirect('repuestover')





#--=======================================Perifericos======================================--

def perifericover(request):
    if request.session.get("id_usuario"):
        listatabla=Perifericos.objects.all()
        listaproveedor = Proveedor.objects.all()
        return validar(request, "productos/perifericover.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Perifericos", "subtitulo_f":"Listado de Perifericos registrados", 
        "listatabla":listatabla, 
        "listaproveedor": listaproveedor})
    else:
        return redirect("login")

def perifericomod(request, periferico_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            listaproveedor = Proveedor.objects.all()
            peri_actual=Perifericos.objects.filter(id_periferico=periferico_actual).exists()
            if peri_actual:
                datos_per=Perifericos.objects.filter(id_periferico=periferico_actual).first()
                return validar(request, "productos/perifericomod.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Periférico", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_per, 
                "periferico_actual":periferico_actual,
                "listaproveedor": listaproveedor})
            else:
                return validar(request, "productos/perifericomod.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Nuevo Periférico", "subtitulo_f":"Por favor complete todos los datos solicitados", 
                "periferico_actual":periferico_actual,
                "listaproveedor": listaproveedor})

        if request.method=="POST":
            if periferico_actual==0:
                perif_nuevo=Perifericos(id_periferico=request.POST.get('id_periferico'),
                cod_periferico=request.POST.get('cod_periferico'),
                tipo_periferico=request.POST.get('tipo_periferico'),
                marca_periferico=request.POST.get('marca_periferico'),
                descripcion_periferico=request.POST.get("descripcion_periferico"),
                nombre_proveedor_id=request.POST.get('proveedor'),
                precio_compra_periferico=request.POST.get('precio_compra_periferico'),
                precio_venta_periferico=request.POST.get('precio_venta_periferico'),
                imagen_periferico=request.FILES.get('imagen_periferico'),
                stock_periferico=request.POST.get('stock_periferico'))

                perif_nuevo.save()
            else:
                periferico_actual=Perifericos.objects.get(id_periferico=periferico_actual)
                periferico_actual.cod_periferico=request.POST.get('cod_periferico')
                periferico_actual.tipo_periferico=request.POST.get('tipo_periferico')
                periferico_actual.marca_periferico=request.POST.get('marca_periferico')
                periferico_actual.descripcion_periferico=request.POST.get('descripcion_periferico')
                periferico_actual.nombre_proveedor_id=request.POST.get('proveedor')
                periferico_actual.precio_compra_periferico=request.POST.get('precio_compra_periferico')
                periferico_actual.precio_venta_periferico=request.POST.get('precio_venta_periferico')
                if request.POST.get('imagen_periferico') != "":
                    periferico_actual.imagen_periferico=request.FILES.get('imagen_periferico')
                else: 
                    periferico_actual.imagen_periferico = periferico_actual.imagen_periferico
                periferico_actual.stock_periferico = request.POST.get('stock_periferico')

                periferico_actual.save() 

        return redirect('perifericover')
    
    else:
        return redirect("login")

def perifericobor(request, periferico_actual):
        Perifericos.objects.filter(id_periferico = periferico_actual).delete()
        return redirect('perifericover')


#--=======================================Placa_Base======================================--

def ver_placa_base(request):
        listatabla = Placa_base.objects.all()
        listaram = Tipo_Ram.objects.all()
        listacpu = Tipo_Cpu.objects.all()
        listagabinete = Tipo_Gabinete.objects.all()
        listaproveedor = Proveedor.objects.all()
        return validar(request, "productos/ver_placa_base.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Placas Base", "subtitulo_f":"Listado de Placas Base registrados", 
        "listatabla":listatabla, 
        "listaram":listaram,
        "listacpu":listacpu,
        "listagabinete":listagabinete,
        "listaproveedor": listaproveedor})

def mod_placa_base(request, placa_base_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            listaram = Tipo_Ram.objects.all()
            listacpu = Tipo_Cpu.objects.all()
            listagabinete = Tipo_Gabinete.objects.all()
            listaproveedor = Proveedor.objects.all()
            peri_actual=Placa_base.objects.filter(id_placa_base=placa_base_actual).exists()
            if peri_actual:
                datos_per=Placa_base.objects.filter(id_placa_base=placa_base_actual).first()
                return validar(request, "productos/mod_placa_base.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Placa Base", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_per, 
                "placa_base_actual":placa_base_actual,
                "listaram":listaram,
                "listacpu":listacpu,
                "listagabinete":listagabinete,
                "listaproveedor": listaproveedor})
            else:
                return validar(request, "productos/mod_placa_base.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Nueva Placa Base", "subtitulo_f":"Por favor complete todos los datos solicitados", 
                "placa_base_actual":placa_base_actual,
                "listaram":listaram,
                "listacpu":listacpu,
                "listagabinete":listagabinete,
                "listaproveedor": listaproveedor})

        if request.method=="POST":
            if placa_base_actual==0:
                perif_nuevo=Placa_base(id_placa_base=request.POST.get('id_placa_base'),
                cod_placa_base=request.POST.get('cod_placa_base'),
                marca_placa_base=request.POST.get('marca_placa_base'),
                descripcion_placa_base=request.POST.get('descripcion_placa_base'),
                nombre_proveedor_id=request.POST.get('proveedor'),
                precio_compra_placa_base=request.POST.get('precio_compra_placa_base'),
                precio_venta_placa_base=request.POST.get('precio_venta_placa_base'),
                tipo_ram_placa_base_id=request.POST.get('tipo_ram_placa_base'),
                tipo_cpu_placa_base_id=request.POST.get('tipo_cpu_placa_base'),
                tipo_gabinete_placa_base_id=request.POST.get('tipo_gabinete_placa_base'),
                imagen_placa_base=request.FILES.get('imagen_placa_base'),
                stock_placa_base=request.POST.get('stock_placa_base'))

                perif_nuevo.save()
            else:
                placa_base_actual=Placa_base.objects.get(id_placa_base=placa_base_actual)
                placa_base_actual.cod_placa_base=request.POST.get('cod_placa_base')
                placa_base_actual.marca_placa_base=request.POST.get('marca_placa_base')
                placa_base_actual.descripcion_placa_base=request.POST.get('descripcion_placa_base')
                placa_base_actual.nombre_proveedor_id=request.POST.get('proveedor')
                placa_base_actual.precio_compra_placa_base=request.POST.get('precio_compra_placa_base')
                placa_base_actual.precio_venta_placa_base=request.POST.get('precio_venta_placa_base')
                placa_base_actual.tipo_ram_placa_base_id=request.POST.get('tipo_ram_placa_base')
                placa_base_actual.tipo_cpu_placa_base_id=request.POST.get('tipo_cpu_placa_base')
                placa_base_actual.tipo_gabinete_placa_base_id=request.POST.get('tipo_gabinete_placa_base')
                placa_base_actual.stock_placa_base=request.POST.get('stock_placa_base')
                if request.POST.get('imagen_placa_base') != "":
                    placa_base_actual.imagen_placa_base=request.FILES.get('imagen_placa_base')
                else: 
                    placa_base_actual.imagen_placa_base = placa_base_actual.imagen_placa_base
                
                placa_base_actual.save() 

        return redirect('ver_placa_base')
    
    else:
        return redirect("login")

def bor_placa_base(request, placa_base_actual):
        Perifericos.objects.filter(id_placa_base = placa_base_actual).delete()
        return redirect('ver_placa_base')

#--=======================================RAM======================================--

def ver_ram(request):
        listatabla = RAM.objects.all()
        listaram = Tipo_Ram.objects.all()
        listaproveedor = Proveedor.objects.all()
        return validar(request, "productos/ver_ram.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Memorias RAM", "subtitulo_f":"Listado de Memorias RAM registradas", 
        "listatabla":listatabla, 
        "listaram":listaram,
        "listaproveedor": listaproveedor})

def mod_ram(request, ram_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            listaram = Tipo_Ram.objects.all()
            listaproveedor = Proveedor.objects.all()
            peri_actual=RAM.objects.filter(id_ram=ram_actual).exists()
            if peri_actual:
                datos_per=RAM.objects.filter(id_ram=ram_actual).first()
                return validar(request, "productos/mod_ram.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Memoria RAM", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_per, 
                "ram_actual":ram_actual,
                "listaram":listaram,
                "listaproveedor": listaproveedor})
            else:
                return validar(request, "productos/mod_ram.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Nueva Memoria RAM", "subtitulo_f":"Por favor complete todos los datos solicitados", 
                "ram_actual":ram_actual,
                "listaram":listaram,
                "listaproveedor": listaproveedor})

        if request.method=="POST":
            if ram_actual==0:
                ram_nuevo=RAM(id_ram=request.POST.get('id_ram'),
                cod_ram=request.POST.get('cod_ram'),
                marca_ram=request.POST.get('marca_ram'),
                descripcion_ram=request.POST.get('descripcion_ram'),
                nombre_proveedor_id=request.POST.get('proveedor'),
                precio_compra_ram=request.POST.get('precio_compra_ram'),
                precio_venta_ram=request.POST.get('precio_venta_ram'),
                tipo_ram_id=request.POST.get('tipo_ram'),
                imagen_ram=request.FILES.get('imagen_ram'),
                stock_ram=request.POST.get('stock_ram'))

                ram_nuevo.save()
            else:
                ram_actual=RAM.objects.get(id_ram=ram_actual)
                ram_actual.cod_ram=request.POST.get('cod_ram')
                ram_actual.marca_ram=request.POST.get('marca_ram')
                ram_actual.descripcion_ram=request.POST.get('descripcion_ram')
                ram_actual.nombre_proveedor_id=request.POST.get('proveedor')
                ram_actual.precio_compra_ram=request.POST.get('precio_compra_ram')
                ram_actual.precio_venta_ram=request.POST.get('precio_venta_ram')
                ram_actual.tipo_ram_id=request.POST.get('tipo_ram')
                if request.POST.get('imagen_ram') != "":
                    ram_actual.imagen_ram=request.FILES.get('imagen_ram')
                else: 
                    ram_actual.imagen_ram = ram_actual.imagen_ram
                ram_actual.stock_ram=request.POST.get('stock_ram')

                ram_actual.save() 

        return redirect('ver_ram')
    
    else:
        return redirect("login")

def bor_ram(request, ram_actual):
        RAM.objects.filter(id_ram = ram_actual).delete()
        return redirect('ver_ram')

#--=======================================CPU======================================--

def ver_cpu(request):
        listatabla = CPU.objects.all()
        listacpu = Tipo_Cpu.objects.all()
        listaproveedor = Proveedor.objects.all()
        return validar(request, "productos/ver_cpu.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Procesadores", "subtitulo_f":"Listado de Procesadores registrados", 
        "listatabla":listatabla, 
        "listacpu":listacpu,
        "listaproveedor": listaproveedor})

def mod_cpu(request, cpu_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            listacpu = Tipo_Cpu.objects.all()
            listaproveedor = Proveedor.objects.all()
            peri_actual=CPU.objects.filter(id_cpu=cpu_actual).exists()
            if peri_actual:
                datos_per=CPU.objects.filter(id_cpu=cpu_actual).first()
                return validar(request, "productos/mod_cpu.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Procesador", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_per, 
                "cpu_actual":cpu_actual,
                "listacpu":listacpu,
                "listaproveedor": listaproveedor})
            else:
                return validar(request, "productos/mod_cpu.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Nuevo Procesador", "subtitulo_f":"Por favor complete todos los datos solicitados", 
                "cpu_actual":cpu_actual,
                "listacpu":listacpu,
                "listaproveedor": listaproveedor})

        if request.method=="POST":
            if cpu_actual==0:
                cpu_nuevo=CPU(id_cpu=request.POST.get('id_cpu'),
                cod_cpu=request.POST.get('cod_cpu'),
                marca_cpu=request.POST.get('marca_cpu'),
                descripcion_cpu=request.POST.get('descripcion_cpu'),
                nombre_proveedor_id=request.POST.get('proveedor'),
                precio_compra_cpu=request.POST.get('precio_compra_cpu'),
                precio_venta_cpu=request.POST.get('precio_venta_cpu'),
                tipo_cpu_id=request.POST.get('tipo_cpu'),
                imagen_cpu=request.FILES.get('imagen_cpu'),
                stock_cpu=request.POST.get('stock_cpu'))

                cpu_nuevo.save()
            else:
                cpu_actual=CPU.objects.get(id_cpu=cpu_actual)
                cpu_actual.cod_cpu=request.POST.get('cod_cpu')
                cpu_actual.marca_cpu=request.POST.get('marca_cpu')
                cpu_actual.descripcion_cpu=request.POST.get('descripcion_cpu')
                cpu_actual.nombre_proveedor_id=request.POST.get('proveedor')
                cpu_actual.precio_compra_cpu=request.POST.get('precio_compra_cpu')
                cpu_actual.precio_venta_cpu=request.POST.get('precio_venta_cpu')
                cpu_actual.tipo_cpu_id=request.POST.get('tipo_cpu')
                if request.POST.get('imagen_cpu') != "":
                    cpu_actual.imagen_cpu=request.FILES.get('imagen_cpu')
                else: 
                    cpu_actual.imagen_cpu = cpu_actual.imagen_cpu
                cpu_actual.stock_cpu=request.POST.get('stock_cpu')

                cpu_actual.save() 

        return redirect('ver_cpu')
    
    else:
        return redirect("login")

def bor_cpu(request, cpu_actual):
        CPU.objects.filter(id_cpu = cpu_actual).delete()
        return redirect('ver_cpu')

#--=======================================Gabinetes======================================--

def ver_gab(request):
        listatabla = Gabinete.objects.all()
        listagabinete = Tipo_Gabinete.objects.all()
        listaproveedor = Proveedor.objects.all()
        return validar(request, "productos/ver_gab.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Gabinetes", "subtitulo_f":"Listado de Gabinetes registrados", 
        "listatabla":listatabla, 
        "listagabinete":listagabinete,
        "listaproveedor": listaproveedor})

def mod_gab(request, gab_actual=0):
    if request.session.get("id_usuario"):
        if request.method=="GET":
            listagabinete = Tipo_Gabinete.objects.all()
            listaproveedor = Proveedor.objects.all()
            peri_actual=Gabinete.objects.filter(id_gab=gab_actual).exists()
            if peri_actual:
                datos_per=Gabinete.objects.filter(id_gab=gab_actual).first()
                return validar(request, "productos/mod_gab.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Modificar Gabinete", 
                "subtitulo_f":"Vuelva a escribir los datos que desea modificar", 
                "datos_act":datos_per, 
                "gab_actual":gab_actual,
                "listagabinete":listagabinete,
                "listaproveedor": listaproveedor})
            else:
                return validar(request, "productos/mod_gab.html", 
                {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
                "titulo_f":"Nuevo Gabinete", "subtitulo_f":"Por favor complete todos los datos solicitados", 
                "gab_actual":gab_actual,
                "listagabinete":listagabinete,
                "listaproveedor": listaproveedor})

        if request.method=="POST":
            if gab_actual==0:
                cpu_nuevo=Gabinete(id_gab=request.POST.get('id_gab'),
                cod_gab=request.POST.get('cod_gab'),
                marca_gab=request.POST.get('marca_gab'),
                descripcion_gab=request.POST.get('descripcion_gab'),
                nombre_proveedor_id=request.POST.get('proveedor'),
                precio_compra_gab=request.POST.get('precio_compra_gab'),
                precio_venta_gab=request.POST.get('precio_venta_gab'),
                tipo_gabinete_id=request.POST.get('tipo_gabinete'),
                imagen_gab=request.FILES.get('imagen_gab'),
                stock_gab=request.POST.get('stock_gab'))

                cpu_nuevo.save()
            else:
                gab_actual=Gabinete.objects.get(id_gab=gab_actual)
                gab_actual.cod_gab=request.POST.get('cod_gab')
                gab_actual.marca_gab=request.POST.get('marca_gab')
                gab_actual.descripcion_gab=request.POST.get('descripcion_gab')
                gab_actual.nombre_proveedor_id=request.POST.get('proveedor')
                gab_actual.precio_compra_gab=request.POST.get('precio_compra_gab')
                gab_actual.precio_venta_gab=request.POST.get('precio_venta_gab')
                gab_actual.tipo_gabinete_id=request.POST.get('tipo_gabinete')
                if request.POST.get('imagen_gab') != "":
                    gab_actual.imagen_gab=request.FILES.get('imagen_gab')
                else: 
                    gab_actual.imagen_gab = gab_actual.imagen_gab
                gab_actual.stock_gab=request.POST.get('stock_gab')

                gab_actual.save() 

        return redirect('ver_gab')
    
    else:
        return redirect("login")

def bor_gab(request, gab_actual):
        Gabinete.objects.filter(id_gab = gab_actual).delete()
        return redirect('ver_gab')
        
#--=======================================Listado_General======================================--

def ver_productos(request):
        listaperiferico = Perifericos.objects.all()
        listagabinete = Gabinete.objects.all()
        listacpu = CPU.objects.all()
        listaram = RAM.objects.all()
        listaplaca = Placa_base.objects.all()
        listarepuesto = Repuestos.objects.all()
        listaproveedor = Proveedor.objects.all()
        return validar(request, "productos/ver_productos.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Productos", "subtitulo_f":"Listado de Productos registrados", 
        "listagabinete":listagabinete,
        "listaperiferico":listaperiferico,
        "listacpu":listacpu,
        "listaram":listaram,
        "listaplaca":listaplaca,
        "listaproveedor":listaproveedor,
        "listarepuesto": listarepuesto})

#--=======================================Inventario======================================--

def inventario(request):
        listaperiferico = Perifericos.objects.all()
        listagabinete = Gabinete.objects.all()
        listacpu = CPU.objects.all()
        listaram = RAM.objects.all()
        listaplaca = Placa_base.objects.all()
        listarepuesto = Repuestos.objects.all()
        listaproveedor = Proveedor.objects.all()
        return validar(request, "inventario.html", 
        {"nombre_completo_usuario":request.session.get("nombre_completo_usuario"), 
        "titulo_f":"Productos", "subtitulo_f":"Listado de Productos registrados", 
        "listagabinete":listagabinete,
        "listaperiferico":listaperiferico,
        "listacpu":listacpu,
        "listaram":listaram,
        "listaplaca":listaplaca,
        "listaproveedor":listaproveedor,
        "listarepuesto": listarepuesto})
 
#--=======================================Validación======================================--
def validar(request, pageSuccess, parameters={}):
    if request.session.get("id_usuario"):
        if (request.session.get("tipo_usuario") == 2) and ((pageSuccess == 'users/verusuario.html') or (pageSuccess == 'maintenance/tipo_cpu/vertipo_cpu.html') or (pageSuccess == 'maintenance/tipo_ram/vertipo_ram.html') or (pageSuccess == 'maintenance/tipo_gabinete/vertipo_gabinete.html')):
            return render(request, "index.html", {"nombre_usuario": request.session.get("nombre_completo_usuario"),"tipo_usuario": request.session.get("tipo_usuario"), "mensaje": "Este usuario no cuenta con los privilegios suficientes"})
        else: 
            return render(request, pageSuccess, {"nombre_usuario": request.session.get("nombre_completo_usuario"),"tipo_usuario": request.session.get("tipo_usuario"), "parameters": parameters})
    else:
        return render(request, 'login.html')



