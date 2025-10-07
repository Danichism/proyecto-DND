
import json

#---------------Funciones auxiliares------------------
"""--------------Funciones de guardado y carga de archivos--------"""
def guardar_en_archivo(nombre_archivo, datos):
    with open (nombre_archivo, "w") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def cargar_archivo(nombre_archivo, mensaje_no_archivo, mensaje_corrupto):
    try:
        with open (nombre_archivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print (mensaje_no_archivo)
        return []
    except json.JSONDecodeError:
        print (mensaje_corrupto)
        return []

"""------------------Funciones para solicitar valores---------------------"""
def solicitar_entero(minimo, maximo, mensaje): #de un valor mínimo a un valor máximo
    while True:
        try:
            numero=int(input(mensaje))
            if numero<minimo or numero>maximo:
                print ("Opción no válida\n")
            else:
                return numero
        except ValueError:
            print ("Opción no válida\n")

def solicitar_numero_positivo(mensaje):
    while True:
        try:
            entero=int(input(mensaje))
            if entero<0:
                print ("Error. Ha introducido un número negativo")
                continue
            return entero
        except ValueError:
            print ("No ha introducido un valor válido")
            continue
"""-------------------Creación de menús-------------------------------"""
def crear_menu(lista_opciones, mensaje):
    if lista_opciones==[]:
        return None
    else:
        for indice, opcion in enumerate(lista_opciones):
            print( f"{indice+1}. {opcion}")
        decision= solicitar_entero(1, len(lista_opciones), mensaje)
        return lista_opciones[decision-1]


def crear_menu_dinamico (lista_opciones, lista_acciones): 
    if len(lista_opciones)!=len(lista_acciones):
        print ("Niño, no coincide el número de opciones con el número de acciones")
        return
    else:
        diccionario_acciones={}
        for indice, opcion in enumerate(lista_opciones):
            print( f"{indice+1}. {opcion}")
        for indice, accion in enumerate(lista_acciones):    
            diccionario_acciones[indice+1]=accion
        decision= solicitar_entero(1, len(lista_opciones), "¿Qué decisión toma?")
        return diccionario_acciones[decision]()

def crear_menu_por_nombre(lista_diccionarios, clave,  mensaje): #Usar cuando generes un menu con lista de diccionarios 
    lista_nombres=[diccionario[clave] for diccionario in lista_diccionarios]
    nombre_seleccionado=crear_menu(lista_nombres, mensaje)
    for diccionario in lista_diccionarios:
        if diccionario[clave]==nombre_seleccionado:
            return diccionario
    return None

def generar_lista(lista_opciones, mensaje): #Genera una lista a partir de serie de opciones
    lista_final=[]
    lista_opciones.append("Salir")
    while True:
        decision=crear_menu(lista_opciones, mensaje)
        if decision=="Salir":
            return lista_final            
        else:
            lista_final.append(decision)
            lista_opciones.remove(decision)

def devolver_booleano(mensaje):
    return crear_menu(["Sí", "No"], mensaje)=="Sí"
    
    
    
            

        
   




            
