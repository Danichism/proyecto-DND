
import random
import json
import funciones_auxiliares



#---------------Funciones auxiliares propias


def generar_diccionario_de_tipos_de_daño(numero_de_tipos_de_daño):
    diccionario_daño={}
    lista_daños=["Cortante", "Perforante", "Contundente", "Radiante", "Veneno", "Fuego", "Hielo"]
    for daño in range (numero_de_tipos_de_daño):
        tipo_de_daño=funciones_auxiliares.crear_menu(lista_daños, "Selecciones el tipo de daño")
        valor_del_tipo_de_daño=funciones_auxiliares.solicitar_numero_positivo(f"Esctiba el valor asociado al daño {tipo_de_daño}")
        diccionario_daño[tipo_de_daño]=valor_del_tipo_de_daño
        lista_daños.remove(tipo_de_daño)
    return diccionario_daño

def crear_arma():  #Se separan los diccionarios según si el arma es cuerpo a cuerpo o a distancia con sus características propias
    tipo_arma=funciones_auxiliares.crear_menu (["Cuerpo a cuerpo", "A distancia"], "Identifica si es un arma cuerpo a cuerpo o a distancia")
    nombre=input("Introduzca el nombre del arma")
    clase_de_arma=funciones_auxiliares.crear_menu (["Sencilla", "Marcial"], "Define el tipo de arma")
    peso=funciones_auxiliares.solicitar_numero_positivo("Introduzca el peso del arma")
    tipos_de_daño=funciones_auxiliares.solicitar_numero_positivo("Cuantos tipos de daño tiene el arma?")
    dict_daño=generar_diccionario_de_tipos_de_daño(tipos_de_daño)
    if tipo_arma=="Cuerpo a cuerpo":
        sutil=funciones_auxiliares.devolver_booleano("¿Es el arma sutil?") 
        arma={"Nombre":nombre, "tipo_de_arma": tipo_arma, "Clase de arma":clase_de_arma, "Daño":dict_daño, "Peso":peso, "Sutil":sutil}
    elif tipo_arma=="A distancia":
        alcance=funciones_auxiliares.solicitar_numero_positivo("Cuál es el alcance del arma?")
        arma={"Nombre":nombre, "tipo_de_arma": tipo_arma, "Clase de arma":clase_de_arma, "Daño":dict_daño, "Peso":peso, "Alcance": alcance}
    return arma

def añadir_a_lista_de_armas(): #Añade diccionario con caraterísticas de un arma a la lista de armas, que se guarda en un archivo .json 
    nueva_arma=crear_arma() 
    lista_actualizada=funciones_auxiliares.cargar_archivo ("lista_de_armas.json", "Se ha creado un archivo nuevo", "El archivo está corrupto")
    lista_actualizada.append(nueva_arma)
    funciones_auxiliares.guardar_en_archivo("lista_de_armas.json", lista_actualizada)
    print ("El arma se ha añadido correctamente")    

def seleccionar_arma():
    tipo_arma=funciones_auxiliares.crear_menu (["Cuerpo a cuerpo", "A distancia"], "¿Qué tipo de arma desea seleccionar?")
    lista_armas_totales=funciones_auxiliares.cargar_archivo("lista_de_armas.json", "No existe el archivo", "El archivo está corrupto")
    lista_armas=[arma for arma in lista_armas_totales if arma["tipo_de_arma"]==tipo_arma]
    arma_seleccionada=funciones_auxiliares.crear_menu_por_nombre(lista_armas, "Nombre", "Qué arma desea escoger?")
    return arma_seleccionada
  

def eliminar_arma():
    lista_armas=funciones_auxiliares.cargar_archivo("lista_de_armas.json", "No existe el archivo", "El archivo está corrupto")
    arma_seleccionada=funciones_auxiliares.crear_menu_por_nombre(lista_armas, "Nombre", "Qué arma desea eliminar?")
    lista_actualizada=[arma for arma in lista_armas if arma!=arma_seleccionada]
    funciones_auxiliares.guardar_en_archivo("lista_de_armas.json", lista_actualizada)
    print ("El arma se ha eliminado correctamente. A continuación se muestra la lista actualizada")
    

#----------------------Clase arma----------------------------

class Arma:
    def __init__(self, dict_caracteristicas):
        self.nombre=dict_caracteristicas["Nombre"]
        self.daño=dict_caracteristicas["Daño"]
        self.peso=dict_caracteristicas["Peso"]
        self.clase_de_arma=dict_caracteristicas["Clase de arma"]
        
    @classmethod
    def from_dict(cls, dict_caracteristicas):
        clasificacion_armas={"Cuerpo a cuerpo": ArmaCuerpoACuerpo, "A distancia": ArmaADistancia}
        tipo_str=dict_caracteristicas.get("tipo_de_arma")
        TIPO_DE_ARMA=clasificacion_armas.get(tipo_str)
        return TIPO_DE_ARMA(dict_caracteristicas)

    def to_dict(self):
        return {"Nombre":self.nombre, "Daño":self.daño, "Peso":self.peso}

    def __str__(self):
        return self.nombre

    def bonificador_ataque(self, personaje):
        """
        Método que las subclases sobrescribirán para su lógica de bonificador.
        """
        raise NotImplementedError("Este método debe ser implementado por la subclase.")


    def calcular_daño(self):
        daño_total=0
        for daño_por_caracterstica  in self.daño:
            daño_total+=random.randint(1, self.daño[daño_por_caracterstica])
        return daño_total

class ArmaCuerpoACuerpo(Arma):
    def __init__(self, dict_caracteristicas):
        super().__init__(dict_caracteristicas)
        self.tipo_arma="Cuerpo a cuerpo"
        self.sutil=dict_caracteristicas.get("Sutil", False)

    def to_dict(self):
        return {"Nombre":self.nombre, "tipo_de_arma": self.tipo_arma, "Clase de arma":self.clase_de_arma, "Daño":self.daño, "Peso":self.peso, "Sutil": self.sutil}

    def bonificador_ataque(self, personaje):
        if self.sutil:
            return max(personaje.bonificacion_caracteristicas["Destreza"], personaje.bonificacion_caracteristicas["Fuerza"])
        else:
            return personaje.bonificacion_caracteristicas["Fuerza"]

class ArmaADistancia(Arma):
    def __init__(self, dict_caracteristicas):
        super().__init__(dict_caracteristicas)
        self.tipo_arma="A distancia"
        self.alcance=dict_caracteristicas.get("Alcance", 18)

    def to_dict(self):
        return {"Nombre":self.nombre, "tipo_de_arma": self.tipo_arma, "Clase de arma":self.clase_de_arma, "Daño":self.daño, "Peso":self.peso, "Alcance": self.alcance}
               

    def bonificador_ataque(self, personaje):
        return personaje.bonificacion_caracteristicas["Destreza"]
        



#-------------bloque principal-------------------------------

if __name__=="__main__":
    
    seguir_creando=True
    while seguir_creando:
        decision=funciones_auxiliares.crear_menu(["Crear_arma", "Seleccionar arma", "Eliminar arma", "Salir"], "¿Qué desea hacer")
        if decision=="Crear_arma":
            añadir_a_lista_de_armas()
        elif decision=="Seleccionar arma":
            arma_seleccionada=seleccionar_arma()
            print (arma_seleccionada)
            print("Gracias por participar")
        elif decision=="Eliminar arma":
            eliminar_arma()
        elif decision=="Salir":
            print("Que tenga un buen día")
            seguir_creando=False
        
        

