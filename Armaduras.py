#------------Librerías----------
import json
import funciones_auxiliares

#---------Funciones para armaduras-----------
def crear_armadura():
    nombre_armadura=input("¿cual es el nombre de la armadura?")
    tipo_de_armadura=funciones_auxiliares.crear_menu(["Ligera", "Intermedia", "Pesada"], "Define el tipo de armadura")
    clase_de_armadura=funciones_auxiliares.solicitar_numero_positivo("¿Cuál es la clase de armadura?")
    lista_resistencias=funciones_auxiliares.generar_lista(["Cortante", "Perforante", "Contundente", "Veneno", "Radiante", "Frío", "Fuego"], "Escoja las resistencias de la armadura")
    dict_armadura={"nombre": nombre_armadura, "tipo_armadura":tipo_de_armadura, "clase_armadura": clase_de_armadura, "lista_resistencias":lista_resistencias}
    return dict_armadura


def generar_lista_armaduras():
    try:
        lista_armaduras=funciones_auxiliares.cargar_archivo("lista_armaduras.json", "No existe el archivo", "El archivo está corrupto")
    except FileNotFoundError:
        lista_armaduras=[]
    nueva_armadura=crear_armadura()
    lista_armaduras.append(nueva_armadura)
    funciones_auxiliares.guardar_en_archivo("lista_armaduras.json", lista_armaduras)
    print ("Se ha añadido la armadura correctamente")

def seleccionar_armadura():
    lista_armaduras=funciones_auxiliares.cargar_archivo("lista_armaduras.json", "No existe el archivo", "El archivo está corrupto")
    armadura=funciones_auxiliares.crear_menu_por_nombre(lista_armaduras, "nombre", "Escoja el armadura")
    return armadura
    



#-------------Clase Armadura---------
class ArmaduraBase:
    def __init__(self, dict_armadura):
        self.nombre=dict_armadura["nombre"]
        self.tipo_armadura=dict_armadura["tipo_armadura"]
        self.clase_armadura=dict_armadura["clase_armadura"]
        self.resistencias=dict_armadura["lista_resistencias"]

    def __str__(self):
        return self.nombre

    @classmethod
    def from_dict(cls, dict_armadura):
        return cls(dict_armadura)

    def to_ditc(self):
        dict_armadura={"nombre": self_nombre, "tipo_armadura":self.tipo_armadura, "clase_armadura": self.clase_armadura, "lista_resistencias":self.resistencias}



class ArmaduraLigera(ArmaduraBase):
    def __init__(self, dict_armadura):
        super().__init__(dict_armadura)
        tipo_armadura="armadura_ligera"

class ArmaduraIntermedia(ArmaduraBase):
    def __init__(self, dict_armadura):
        super().__init__(dict_armadura)
        tipo_armadura="armadura_intermedia"

class ArmaduraPesada(ArmaduraBase):
    def __init__(self, dict_armadura):
        super().__init__(dict_armadura)
        tipo_armadura="armadura_pesada"        

    
        
    




#-----------Bloque principal-------
if __name__=="__main__":
    """dict_armadura=crear_armadura()
    print (dict_armadura)
    if dict_armadura["tipo_armadura"]=="Ligera":
        nueva_armadura=ArmaduraLigera(dict_armadura)
    elif dict_armadura["tipo_armadura"]=="Intermedia":
        nueva_armadura=ArmaduraIntermedia(dict_armadura)
    elif dict_armadura["tipo_armadura"]=="Pesada":
        nueva_armadura=ArmaduraPesada(dict_armadura)


    print (nueva_armadura.tipo_armadura)
    print (nueva_armadura)
    print (nueva_armadura.clase_armadura)"""
    generar_lista_armaduras()



