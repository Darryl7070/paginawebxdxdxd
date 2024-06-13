import pandas as pd
import numpy as np
import streamlit as st
import openpyxl as op
import random as rn
import os as o
import io
from streamlit_option_menu import option_menu
from shutil import rmtree as rma

#Funciones de administrador
def Crear_Rut():
    digitos1 = rn.randint(1,22)
    digitos2 = rn.randint(100,999)
    digitos3 = rn.randint(100,999)
    digito = rn.randint(0,9)
    if digito == 0:
        digito = "k"
    Rut = (f"{digitos1}.{digitos2}.{digitos3}-{digito}")
    return Rut

def Crear_Nombre():
    documento = open("Proyecto1\\Utilidades\\Nombres.txt")
    lista = []
    for i in range(100):
        linea = documento.readline()
        linea = linea.strip("\n")
        lista.append(linea)
    Nombre = lista[rn.randint(0,99)]
    documento.close()
    return Nombre

def Crear_Apellido():
    documento = open("Proyecto1\\Utilidades\\Apellidos.txt")
    lista = []
    for i in range(100):
        linea = documento.readline()
        linea = linea.strip("\n")
        lista.append(linea)
    Apellido = lista[rn.randint(0,99)]
    documento.close()
    return Apellido

def Crear_Servicio():
    documento = open("Proyecto1\\Utilidades\\Cargo.txt")
    lista = []
    for i in range(10):
        linea = documento.readline()
        linea = linea.strip("\n")
        lista.append(linea)
    Cargo = lista[rn.randint(0,9)]
    documento.close()
    return Cargo

def Carpetas_Personal(NombreTrabajador,Rut):
    o.mkdir(f"Proyecto1\Clientes\{Rut}")
    Documento = open(f"Proyecto1\Clientes\{Rut}\Información.txt","x")
    Documento = open(f"Proyecto1\Clientes\{Rut}\Información.txt","w")
    Nombre=(f"{NombreTrabajador} {Crear_Apellido()}")
    Edad = rn.randint(20,80)
    Servicio=Crear_Servicio()
    Solicitudes = rn.randint(1,10)
    Pagos = rn.randint(0,Solicitudes)
    Documento.write(f"{Nombre},{Rut},{Edad},{Servicio},{Solicitudes},{Pagos}")

def Crear_Personas(numero):
    documento = open("Proyecto1\\Clientes\\Rut.txt")
    linea = documento.readline()
    Lista = []
    while linea != "":
        Lista.append(linea)
        linea = documento.readline().strip("\n")
        linea.strip("\n")

    documento = open("Proyecto1\\Clientes\\Rut.txt","a")

    for i in range(numero):
        Rut = Crear_Rut()
        try:
            Lista.index(Rut)
            print("El usuario ya existe.")
            i -= 1
        except:
            Nombre = Crear_Nombre()
            Carpetas_Personal(Nombre,Rut)
            documento.write(f"{Rut}\n")
    documento.close()

def Elementos_Comprados():
    elementos = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(elementos)):
        elementos[i] = rn.randint(80,100)

    return elementos

def Crear_Exel_Gastos(año):
    exel = op.Workbook()
    exel.save(f"Proyecto1\GastosMensuales\Año {año}\Gastos año {año}.xlsx")

def Generar_Gastos():
    
    mes = ["1-Enero","2-Febrero","3-Marzo","4-Abril","5-Mayo","6-Junio","7-Julio","8-Agosto","9-Septiembre","10-Octubre","11-Noviembre","12-Diciembre"]
    elementos = ["Insumos","Transporte","Pagos Empresas Externos","Alojamiento","EPP","Colaciones","Gastos Basicos (Agua, Luz, Etc.)","Maquinaria","Salarios","Gastos Legales"]
    sensibilidades = [200,50,100,50,20,30,150,100,200,50]
    MontoMensual = 0
    for i in range(2000,2025):
        lista=[]
        if not o.path.exists(f"Proyecto1\GastosMensuales\Año {i}"):
            o.mkdir(f"Proyecto1\GastosMensuales\Año {i}")
        Crear_Exel_Gastos(i)
        for x in range(12):
            if not o.path.exists(f"Proyecto1\GastosMensuales\Año {i}\{mes[x]}"):
                o.mkdir(f"Proyecto1\GastosMensuales\Año {i}\{mes[x]}")
                Archivo = open(f"Proyecto1\GastosMensuales\Año {i}\{mes[x]}\GastosDelMes.txt","x")

            Archivo = open(f"Proyecto1\GastosMensuales\Año {i}\{mes[x]}\GastosDelMes.txt","a")
            MontoMensual = Elementos_Comprados()
            for z in range(len(MontoMensual)):
                MontoMensual = Elementos_Comprados()
                for y in range(10):
                    MontoMensual[y] *= sensibilidades[y]
                Archivo.write(f"{elementos[z]}: {str(MontoMensual[z])}\n")
            lista.append(MontoMensual)

        Df = pd.DataFrame(lista,columns=elementos,index=mes)
        Df.to_excel(fr"Proyecto1\GastosMensuales\Año {i}\Gastos año {i}.xlsx")

def Elementos_Comprados():
    elementos = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(elementos)):
        elementos[i] = rn.randint(80,100)

    return elementos

def Crear_Exel_Ingresos(año):
    exel = op.Workbook()
    exel.save(f"Proyecto1\IngresosMensuales\Año {año}\Ingresos año {año}.xlsx")

def Generar_Ingresos():
    
    mes = ["1-Enero","2-Febrero","3-Marzo","4-Abril","5-Mayo","6-Junio","7-Julio","8-Agosto","9-Septiembre","10-Octubre","11-Noviembre","12-Diciembre"]
    elementos = ["Ventas Productos","Transporte","Trabajos Privados","Renta","Renmuneraciones","Trabajos Sociales","Prestación de Maquinaria","Venta Comida","Venta Insumos","Bonos Estatales"]
    sensibilidades = [250,100,90,40,10,10,200,50,250,30]
    MontoMensual = 0
    for i in range(2000,2025):
        lista=[]
        if not o.path.exists(f"Proyecto1\IngresosMensuales\Año {i}"):
            o.mkdir(f"Proyecto1\IngresosMensuales\Año {i}")
        Crear_Exel_Ingresos(i)
        for x in range(12):
            if not o.path.exists(f"Proyecto1\IngresosMensuales\Año {i}\{mes[x]}"):
                o.mkdir(f"Proyecto1\IngresosMensuales\Año {i}\{mes[x]}")
                Archivo = open(f"Proyecto1\IngresosMensuales\Año {i}\{mes[x]}\IngresosDelMes.txt","x")

            Archivo = open(f"Proyecto1\IngresosMensuales\Año {i}\{mes[x]}\IngresosDelMes.txt","a")
            MontoMensual = Elementos_Comprados()
            for z in range(len(MontoMensual)):
                MontoMensual = Elementos_Comprados()
                for y in range(10):
                    MontoMensual[y] *= sensibilidades[y]
                Archivo.write(f"{elementos[z]}: {str(MontoMensual[z])}\n")
            lista.append(MontoMensual)

        Df = pd.DataFrame(lista,columns=elementos,index=mes)
        Df.to_excel(fr"Proyecto1\IngresosMensuales\Año {i}\Ingresos año {i}.xlsx")

def Eliminar_Carpeta(Carpeta):
    rma(f"Proyecto1\{Carpeta}")

#Funciones de la página
def Leer_Exel_Por_Año(Ruta,Año, Metodo):
    if o.path.exists(f"Proyecto1\{Ruta}\Año {Año}\{Metodo} año {Año}.xlsx"):
        Arch = pd.read_excel(f"Proyecto1\{Ruta}\Año {Año}\{Metodo} año {Año}.xlsx")
        return Arch
    else:
        Arch = pd.DataFrame()
        return Arch
def Leer_Datos_Cliente(Rut):
    if o.path.exists(f"Proyecto1\Clientes\{Rut}\Información.txt"):
        Arch = open(f"Proyecto1\Clientes\{Rut}\Información.txt")
        return Arch
    else:
        Arch = False
        return Arch

def Crear_Datos_Cliente(Nombre, Apellido, Rut, Edad, Servicio,Veces_Solicitado, Pagos):
    o.mkdir(f"Proyecto1\Clientes\{Rut}")
    Documento = open(f"Proyecto1\Clientes\{Rut}\Información.txt","x")
    Documento = open(f"Proyecto1\Clientes\{Rut}\Información.txt","w")
    Documento.write(f"{Nombre} {Apellido},{Rut},{Edad},{Servicio},{Veces_Solicitado},{Pagos}")
    Documento = open("Proyecto1\Clientes\Rut.txt","a")
    Documento.write(f"{Rut}\n")
    Documento.close()

def Seguimiento_De_Pagos():
    pass

st.title("Funciones administrativas")

Mes = ["01-Enero","02-Febrero","03-Marzo","04-Abril","05-Mayo","06-Junio","07-Julio","08-Agosto","09-Septiembre","10-Octubre","11-Noviembre","12-Diciembre"]
Gastos = ["Insumos","Transporte","Pagos Empresas Externos","Alojamiento","EPP","Colaciones","Gastos Basicos (Agua, Luz, Etc.)","Maquinaria","Salarios","Gastos Legales"]
Ingresos = ["Ventas Productos","Transporte","Trabajos Privados","Renta","Renmuneraciones","Trabajos Sociales","Prestación de Maquinaria","Venta Comida","Venta Insumos","Bonos Estatales"]

with st.sidebar:
    Opcion = option_menu("Seleccione una operación:",["Facturas","Clientes","Analisis","Funciones de Administrador"])
if Opcion == "Facturas":
    Operacion = st.radio("Elija una opción:",["Generación de Facturas","Seguimiento de Pagos"])
    
    if Operacion == "Generación de Facturas":
        st.subheader("Generación de Facturas")
        Año = st.number_input("Ingrese el año a buscar:",2000,2024)
        
        if st.button("Buscar") and not Leer_Exel_Por_Año("GastosMensuales",Año, "Gastos").empty:
            Arch = Leer_Exel_Por_Año("GastosMensuales",Año, "Gastos")
            st.write(Arch)
            buffer= io.BytesIO()
            with pd.ExcelWriter(buffer) as writer:
                Arch.to_excel(writer, sheet_name=f"Gastos año {Año}", index=False)
        
            st.subheader("Descarga Informe de Gastos")
            st.download_button(
                label= "Descargar:",
                data= buffer,
                file_name= f"Informe de Gastos año {Año}.xlsx",
                mime="application/vnd.ms-exel")

        elif Leer_Exel_Por_Año("GastosMensuales",Año, "Gastos").empty:
            st.warning("No se encontró el archivo.")
    
    elif Operacion == "Seguimiento de Pagos":
        ArchRut = open("Proyecto1\\Clientes\\Rut.txt")
        Servicio = ["Ventas Productos","Transporte","Trabajos Privados","Renta","Renmuneraciones","Trabajos Sociales","Prestación de Maquinaria","Venta Comida","Venta Insumos","Bonos Estatales"]
        Sensibilidades = [2500,1000,900,400,100,100,2000,500,2500,300]
        Nombre = []
        Datos = []
        Rut = ArchRut.readline().strip("\n")
        while Rut != "":
            Ss = 0
            Arch = open(f"Proyecto1\\Clientes\\{Rut}\\Información.txt")
            Linea = Arch.readline().strip("\n").split(",")
            Rut = ArchRut.readline().strip("\n")
            for i in range(10):
                if Linea[3] == Servicio[i]:
                    Ss = Sensibilidades[i]
            Nombre.append(Linea[0])
            Datos.append([Linea[3],Linea[4],Linea[5],int(Linea[4]) - int(Linea[5]),(int(Linea[4]) - int(Linea[5])) * Ss])
        Df = pd.DataFrame(Datos, columns=["Servicio","Veces Solicitados","Pagos Realizados","Pagos Atrazados","Deuda"], index=Nombre)
        st.write(Df)
        ArchRut.close()
        Arch.close()

if Opcion == "Clientes":
    Operacion = st.radio("Elija una opción:",["Registro de Datos","Visualización de Datos","Historial","Informes"])
    if Operacion == "Registro de Datos":
        st.subheader("Ingrese sus datos:")
        Nombre = st.text_input("Ingrese su Nombre:")
        Apellido = st.text_input("Ingrese su Apellido:")
        Edad = st.number_input("Ingrese su Edad:",np.nan)
        Rut = st.text_input("Ingrese su Rut(Con el formato x.xxx.xxx-x):")
        Servicio =  st.selectbox("Ingrese el Servicio Solicitado:",["Ventas Productos","Transporte","Trabajos Privados","Renta","Renmuneraciones","Trabajos Scoiales","Prestación de Maquinaria","Venta Comida","Venta Insumos","Bonos Estatales"])
        Veces_Solicitado = st.text_input("Ingrese la Cantidad Del Servicio Solicitado:")
        Pagos = st.number_input("Ingrese los Pagos Realizados:",np.nan)
        if st.button("Crear"):
            Arch = Leer_Datos_Cliente(Rut)
            if not Arch == False:
                linea = Arch.readline().split(",")
                st.warning(f"El usuario {linea[0]} rut {Rut} ya existe.")
                Arch.close()
            else:
                Crear_Datos_Cliente(Nombre, Apellido, Rut, Edad, Servicio,Veces_Solicitado,Pagos)
                st.success("Usuario Registrado con Éxito.")

    
    elif Operacion == "Visualización de Datos":
        st.subheader("Datos de Clientes")
        try:    
            ArchRut = open("Proyecto1\\Clientes\\Rut.txt")
            Nombre = []
            Datos = []
            Rut = ArchRut.readline().strip("\n")
            while Rut != "":
                Arch = open(f"Proyecto1\\Clientes\\{Rut}\\Información.txt")
                Linea = Arch.readline().strip("\n").split(",")
                Rut = ArchRut.readline().strip("\n")
                Nombre.append(Linea[0])
                Datos.append([Linea[1],Linea[2],Linea[3],Linea[4],Linea[5]])
            Df = pd.DataFrame(Datos, columns=["Rut","Edad","Servicio","Veces Solicitados","Pagos Realizados"], index=Nombre)
            st.write(Df)
            ArchRut.close()
            Arch.close()

        except:
            st.warning("No existe un registro de clientes.")

    elif Operacion == "Historial":
        
        pass

    elif Operacion == "Informe":
        pass
        
if Opcion == "Analisis":
    Operacion = st.radio("Elija una opción:",["Ingresos","Gastos","Resumen del año"])

    if Operacion == "Ingresos":
        st.subheader("Gráfico de Ingresos")
        Año = st.text_input("Ingrese el año a Graficar:",2000,2024)
        
        if st.button("Graficar"):
            if not Leer_Exel_Por_Año("IngresosMensuales",Año, "Ingresos").empty:
                Arch = Leer_Exel_Por_Año("IngresosMensuales",Año, "Ingresos")
                Grafico = []
                for i in range(12):
                    lista = []
                    linea = Arch.iloc[i]
                    for x in range(1,11):
                        lista.append(linea[x])
                    Grafico.append(lista)
                Grafico = pd.DataFrame(Grafico, columns=Ingresos, index=Mes)
                st.bar_chart(Grafico, height=500, width=1000)
                st.write(Grafico)

            else:
                st.warning(f"No se encontró un registro del año {Año}.")

    elif Operacion == "Gastos":
        st.subheader("Gráfico de Gastos")
        Año = st.text_input("Ingrese el año a Graficar:",2000,2024)
        
        if st.button("Graficar"):
            if not Leer_Exel_Por_Año("GastosMensuales",Año, "Gastos").empty:
                Arch = Leer_Exel_Por_Año("GastosMensuales",Año, "Gastos")
                Grafico = []
                for i in range(12):
                    lista = []
                    linea = Arch.iloc[i]
                    for x in range(1,11):
                        lista.append(linea[x])
                    Grafico.append(lista)
                Grafico = pd.DataFrame(Grafico, columns=Gastos, index=Mes)
                st.bar_chart(Grafico, height=500, width=1000)
                st.write(Grafico)
            else:
                st.warning(f"No se encontró un registro del año {Año}.")

    elif Operacion == "Resumen del año":
        st.subheader("Resumen del año")
        Año = st.text_input("Ingrese el año a graficar:",2000,2024)

        if st.button("Graficar"):
            if not Leer_Exel_Por_Año("GastosMensuales",Año, "Gastos").empty and not Leer_Exel_Por_Año("IngresosMensuales",Año, "Ingresos").empty:
                Arch1 = Leer_Exel_Por_Año("IngresosMensuales",Año,"Ingresos")
                Arch2 = Leer_Exel_Por_Año("GastosMensuales",Año,"Gastos")
                Df = []
                Grafico = []
                for i in range(12):
                    lista = []
                    linea1 = Arch1.iloc[i]
                    linea2 = Arch2.iloc[i]
                    for x in range(1,11):
                        lista.append(int(linea1[x])-int(linea2[x]))
                    Df.append(lista)
                for i in range(12):
                    acum = 0
                    linea = Df[i]
                    for x in range(10):
                        acum += linea[x]
                    Grafico.append(acum)

                Grafico = pd.DataFrame(Grafico,index=Mes)
                st.bar_chart(Grafico, height=500, width=1000, color="#60B787")
            
            else:
                st.warning(f"No se encontraron los archivos del año {Año}.")
    
if Opcion == "Funciones de Administrador":
    Operacion = st.radio("Elija una opción",["Gestionar Ingresos", "Gestionar Gastos","Crear Base de Datos Aleatoria","Crear Clientes Aleatorios","Eliminar Base de Datos"])

    if Operacion == "Gestionar Ingresos":

       
        Ing = st.selectbox("Elija una opción:",["Crear Año","Crear Mes","Modificar Año","Modificar Mes"])
            
        if Ing == "Crear Año":
                Año = st.number_input("Ingrese un año:",2000,2024)

        elif Ing == "Crear Mes":
            pass

        elif Ing == "Modificar Año":
            Año = st.number_input("Ingrese un año:",2000,2024)


        elif Ing == "Modificar Mes":
            pass

    elif Operacion == "Gestionar Gastos":
        
        
        Gas = st.selectbox("Elija una opción:",["Crear Año","Crear Meses","Modificar Año","Modificar Meses"])
        
        if Gas == "Crear Año":
                Año = st.number_input("Ingrese un año:",2000,2024)

                if st.button("Crear Año"):
                    if not o.path.exists(f"Proyecto1\GastosMensuales\Año {Año}"):
                        o.mkdir(f"Proyecto1\GastosMensuales\Año {Año}")
                        Crear_Exel_Gastos(Año)
                        st.success("El año se ha creado exitosamente.")

                    else:
                        st.warning("El año ya existe.")

        elif Gas == "Crear Meses":
            Meses = st.selectbox("Elija una opción:",["Mes","Año Completo"])
            if Meses == "Mes":
                st.write("Esta función genera una carpeta del mes seleccionado.")
                Año = st.number_input("Ingrese el año:",2000,2024)
                mes = st.radio("Elija el mes:",Mes)
                
                if st.button("Crear mes"):
                    if o.path.exists(f"Proyecto1\GastosMensuales\Año {Año}") and not o.path.exists(f"Proyecto1\GastosMensuales\Año {Año}\{mes}"):    
                        o.mkdir(f"Proyecto1\GastosMensuales\Año {Año}\{mes}")
                        st.success("Mes creado exitosamente.")
                
                    elif not o.path.exists(f"Proyecto1\GastosMensuales\Año {Año}"):
                        st.warning("El año seleccionado no exite en los registros.")
                
                    elif o.path.exists(f"Proyecto1\GastosMensuales\Año {Año}\{mes}"):
                        st.warning("Ya existe un registro del mes.")
            
            elif Meses == "Meses":    
                st.write("Esta función genera una carpeta con un archivo de información vacio por cada mes del año, todo esto en la carpeta seleccionada.")
            

        elif Gas == "Modificar Año":
            Año = st.number_input("Ingrese un año:",2000,2024)


        elif Gas == "Modificar Mes":
            pass

    elif Operacion == "Eliminar Base de Datos":
        st.write("Esta función elimina las carpetas \"IngresosMensuales\", \"GastosMensuales\" y \"Clientes\".")

        if st.button("Eliminar Base de Datos"):
            Eliminar_Carpeta("IngresosMensuales")
            Eliminar_Carpeta("GastosMensuales")
            Eliminar_Carpeta("Clientes")
            o.mkdir("Proyecto1\IngresosMensuales")
            o.mkdir("Proyecto1\GastosMensuales")
            o.mkdir("Proyecto1\Clientes")
            open("Proyecto1\Clientes\Rut.txt","x")
            st.success("Carpetas Eliminadas.")

    elif Operacion == "Crear Base de Datos Aleatoria":
        st.write("Esta función genera una base de datos de ingresos aleatorios desde el año 2000 al año 2024. Cumple el proposito de probar las funcionalidades del código detectar errores.")
        
        if st.button("Crear Base de Datos"):
            Generar_Gastos()
            Generar_Ingresos()
            st.success("Base de Datos Creada.")
    
        
    elif Operacion == "Crear Clientes Aleatorios":
        st.write("Esta función genera clientes con Nombre, Apellido, Rut, Edad, Servivio Solicitado, Cantidad de Servicios Solicitados y Pagos Realizados aleatorios.")
        numero = st.number_input("Ingrese cantidad de Clientes a crear:", np.nan)
        
        if st.button("Crear Clientes") and numero > 0:
            Crear_Personas(int(numero))
            st.success(f"Los {numero} Clientes aleatoros han sido creados.")

