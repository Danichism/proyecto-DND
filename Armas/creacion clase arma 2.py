import json
import random

#Este programa es para crear objetos de la clase arma a partir de un archivo.json


#-------------funciones auxiliares---------------------------
def cargar_archivo(nombre_archivo):
    try:
        with open (nombre_archivo, "r")as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def buscar_arma(lista_armas, arma_buscada):
    for arma in lista_armas:
        if arma["Nombre"]==arma_buscada:
            return arma
    return None
        

def crear_menu(lista_opciones, mensaje):
    if lista_opciones==[]:
        #print ("Lista vacía")
        return None
    else:
        for indice, opcion in enumerate(lista_opciones):
            print( f"{indice+1}. {opcion}")
        decision= solicitar_entero(1, len(lista_opciones), mensaje)
        return lista_opciones[decision-1]

def crear_menu_armas(lista_dict_armas):
    lista_nombre_armas=[]
    for arma in lista_dict_armas:
        lista_nombre_armas.append(arma["Nombre"])
    return crear_menu(lista_nombre_armas,"¿Qué arma escoge?")
        

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

    

#-------------Definición de la clase armadura y sus métodos---------

class Arma:
    def __init__(self, dict_caracteristicas):
        self.nombre=dict_caracteristicas["Nombre"]
        self.daño=dict_caracteristicas["Daño"]
        self.peso=dict_caracteristicas["Peso"]


    @classmethod
    def from_dict(cls, dict_caracteristicas):
        return cls(dict_caracteristicas)

    def calcular_daño(self):
        daño_total=0
        for daño_por_caracterstica  in self.daño:
            daño_total+=random.randint(1, self.daño[daño_por_caracterstica])
        return daño_total
        

        

#---------------------------------------------Cuerpo principal-------------------------
if __name__=="__main__":
    decision=crear_menu(["Crear un objeto arma", "Salir"], "¿Qué desea hacer?")
    if decision=="Crear un objeto arma":
        lista_armas=cargar_archivo("lista_de_armas.json")
        arma=crear_menu_armas(lista_armas)
        arma_buscada=(buscar_arma(lista_armas, arma))   
        if arma_buscada:
            mi_arma=Arma.from_dict(arma_buscada)
            print (f"El arma es {mi_arma.nombre}. Tiene un peso de {mi_arma.peso}")
            print(f"Has hecho {mi_arma.calcular_daño()} puntos de daño")
        else:
            print("El arma no se encuentra en la lista o el archivo de armas no existe o está dañado")   
    elif decision=="Salir":
        print("No pasa nada, otro día creará el arma")
        
    
