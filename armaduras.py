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
        tipos_de_armadura={"Ligera": ArmaduraLigera, "Intermedia":ArmaduraIntermedia, "Pesada": ArmaduraPesada}
        tipo_armadura_str=dict_armadura.get("tipo_armadura")
        tipo_armadura_objeto=tipos_de_armadura.get(tipo_armadura_str)
        return tipo_armadura_objeto(dict_armadura)

    def to_dict(self):
        dict_armadura={"nombre": self_nombre, "tipo_armadura":self.tipo_armadura, "clase_armadura": self.clase_armadura, "lista_resistencias":self.resistencias}

    def calcular_CA_base (self, destreza_del_personaje):
        """
    Método que las subclases sobrescribirán para su lógica de bonificador.
    """
        raise NotImplementedError("Este método debe ser implementado por la subclase.")



class ArmaduraLigera(ArmaduraBase):
    def __init__(self, dict_armadura):
        super().__init__(dict_armadura)

    def calcular_CA_base (self, destreza_del_personaje):
        return destreza_del_personaje+self.clase_armadura

class ArmaduraIntermedia(ArmaduraBase):
    def __init__(self, dict_armadura):
        super().__init__(dict_armadura)

    def calcular_CA_base (self, destreza_del_personaje):
        return min (destreza_del_personaje, 2)+self.clase_armadura

class ArmaduraPesada(ArmaduraBase):
    def __init__(self, dict_armadura):
        super().__init__(dict_armadura)

    def calcular_CA_base (self, destreza_del_personaje):
        return self.clase_armadura

class SinArmadura(ArmaduraBase):
    def __init__(self):
        super().__init__({"nombre": "No lleva armadura", "tipo_armadura":"Sin armadura", "clase_armadura": 0, "lista_resistencias":[]})

    def calcular_CA_base (self, destreza_del_personaje):
        return destreza_del_personaje
    
        
    




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



