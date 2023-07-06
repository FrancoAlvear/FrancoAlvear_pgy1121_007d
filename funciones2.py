import numpy as np
import msvcrt

lista_ruts_asistentes = {}
lista_asistentes = {}
lista_ruts = {}
lista_nombres = {}
lista_apellidos = {}
lista_filas = {1,2,3,4,5,6,7,8,9,10}
lista_columnas = {1,2,3,4,5,6,7,8,9,10}

cantidad_entradas_platinum = 0
cantidad_entradas_gold = 0
cantidad_entradas_silver = 0

valor_entradas_platinum = 120000
valor_entradas_gold = 80000
valor_entradas_silver = 50000



escenario = np.zeros((10,10),int)


def menu():
    print("""
    Menú
    1.  Comprar entradas
    2.  Mostrar ubicaciones disponibles
    3.  Ver listado de asistentes
    4.  Mostrar ganancias totales
    5.  Salir""")


def opciones():
    while True:
        try:
            opc = int(input("Ingrese la opcion: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("ERROR! debe ingresar una de las opciones mostradas en pantalla")
        except:
            print("ERROR! debe ser un numero entero")


def validacion_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip) > 2 and nombre.isalpha:
            return nombre
        else:
            ("ERROR su nomre debe contener MINIMO 3 LETRAS")


def validacion_apellido():
    while True:
        apellido = input("Ingrese su apellido: ")
        if len(apellido.strip) > 2 and apellido.isalpha:
            return apellido
        else:
            print("ERROR! el apellido debe contener MINIMO 3 LETRAS") 


def validacion_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut sin puntos nio guiones ejemplo (12345678): "))
            if (str(rut)) > 1000000 and (str(rut)) < 99999999:
                return rut
            else:
                print("ERROR! el rut es sin caracteres especiales")
        
        except:
            print("ERROR! debe ser un rut valido que oscile entere 1000000 y 99999999")



def ver_ubicaciones():
    print("Columna 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
    for x in range(10):
            print("fila",{x+1}, end="")
    for y in range(10):
            print(escenario,{x}{y}, end ="")
    print("")
    print("Presione cualquier tecla para continuar")
    msvcrt.getch()


def validacion_fila():
    while True:
        try:
            fila = int(input("Ingrese la fila: "))
            if fila in lista_filas:
                return fila
            else:
                print("ERROR! debe encontrarse la fila registrada")
        except:
            print("ERROR! debe ser un numero entero")


def validacion_columnas():
    while True:
        try:
            columna = int(input("Ingrese la columna: "))
            if columna in lista_columnas:
                return columna
            else:
                print("ERROR! debe encontrarse la columna registrada")
        except:
            print("ERROR! debe ser un numero entero")


def comprar_entradas():
    print("Ingrese sus datos para la compra de entradas")
    nombre = validacion_nombre()
    apellido = validacion_apellido()
    rut = validacion_rut()
    cantidad_entradas_platinum = int(input("Ingrese la cantidad de entradas platinum que quiere (120.000$): "))
    cantidad_entradas_gold = int(input("Ingrese la cantidad de entradas gold que quiere (80.000$): "))
    cantidad_entradas_silver = int(input("Ingrese la cantidad de entradas silver que quiere (50.000$): "))
    ver_ubicaciones()
    while True:
        fila = validacion_fila()
        columna = validacion_columnas()
        if escenario {fila -1} {columna -1} == 0:
            escenario {fila -1} {columna -1} = 1
            lista_nombres.append(nombre)
            lista_apellidos.append(apellido)
            lista_ruts.append(rut)



def validacion_asistenetes():
    print(f"""esta es la lista de asistentes: 
    RUN: {lista_ruts_asistentes.append} Nombre: {lista_asistentes}""")
    

def ganancias_totales():
    while True:
        entradas_platinum = cantidad_entradas_platinum * valor_entradas_platinum
        entradas_gold = cantidad_entradas_gold * valor_entradas_gold
        entradas_silver = cantidad_entradas_silver * valor_entradas_silver
        cantiad_total = cantidad_entradas_platinum + cantidad_entradas_gold + cantidad_entradas_silver
        total_entradas = entradas_platinum + entradas_gold + entradas_silver
        print("Las ganancias totales son las siguientes")
        print(f"""
        _________________________________________________________________
        |tipo entrada|Cantidad de entradas compradas|  Total de entrada |    
        |Platinum    |{cantidad_entradas_platinum}  |{entradas_platinum}| 
        |Gold        |{cantidad_entradas_gold}      |{entradas_gold}    |
        |silver      |{cantidad_entradas_gold}      |{entradas_silver}  |
        _________________________________________________________________
        TOTAL        |{cantiad_total}               |{total_entradas}   |
        -----------------------------------------------------------------""")


def salir():
    nombre = validacion_nombre
    apellido = validacion_apellido
    print(f"Salida del sistema exitosa sr(a) {lista_nombres} {lista_apellidos}")





