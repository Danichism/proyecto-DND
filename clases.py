import armaduras
import funciones_auxiliares
import json

#-------------------------------FUNCIONES PROPIAS PARA LA CREACIÓN DE LAS CLASES------------------------------------------------------------------------------------------------------------------------------------
def escoger_clase_DND():
    clases_disponibles=[Barbaro(), Bardo(), Brujo(), Clerigo()] #Lista donde se añaden las clases de d&d
    clase_escogida=funciones_auxiliares.crear_menu(clases_disponibles, "¿Qué clase escoge?")
    return clase_escogida



#-------------------------------CREACIÓN DE LAS DIFERENTES CLASES------------------------------------------------------------------------------------------------------------------------------------



#-------------------------Se crea la clase para las diferentes clases en DND------------
class ClaseBase:
    def __init__ (self, nombre,  dado_de_golpe):
        self.nombre=nombre
        self.dado_de_golpe=dado_de_golpe

    def bonificador_clase_armadura (self, bonificaciones_caracteristicas, armadura_equipada):
        return 0

    def __str__(self):
        return self.nombre

    @classmethod
    def from_dict(cls, dict_clase):
        clases_del_juego={"Bárbaro": Barbaro, "Bardo": Bardo, "Brujo": Brujo, "Clérigo": Clerigo, "Clase_base":ClaseBase}
        clase_str=dict_clase.get("Nombre", "Clase_base")
        clase_objeto=clases_del_juego.get(clase_str)
        nombre=dict_clase["Nombre"]
        dado_de_golpe=dict_clase["Dado_de_golpe"]
        return clase_objeto()

    def to_dict(self):
        return {"Nombre":self.nombre, "Dado_de_golpe":self.dado_de_golpe}
       
            

class Barbaro (ClaseBase):
    def __init__ (self):
        super().__init__ ("Bárbaro", 12)  

    def bonificador_clase_armadura (self, bonificaciones_caracteristicas, armadura_equipada):
        if isinstance (armadura_equipada,armaduras.SinArmadura):
            return bonificaciones_caracteristicas["Constitución"] 
        else:
            return 0 

class Bardo (ClaseBase):
    def __init__ (self):
        super().__init__ ("Bardo", 8)

class Brujo (ClaseBase):
    def __init__ (self):
        super().__init__("Brujo", 8)
        
class Clerigo (ClaseBase):
    def __init__ (self):
        super().__init__("Clérigo", 8)
        

#-------------Construción de las clases de d&d como objetos-----------------
if __name__=="__main__":
    """lista_clases=[Barbaro(), Bardo(), Brujo(), Clerigo()]
    lista_diccionarios=[]
    for clase in lista_clases:
        print(clase)
        print (clase.dado_de_golpe)
        print(f"{clase.dado_de_golpe}")
        nuevo_diccionario=clase.to_dict()
        lista_diccionarios.append(nuevo_diccionario)
    funciones_auxiliares.guardar_en_archivo("clases_DND_disponibles.json", lista_diccionarios)        
    print("Se ha creado el archivo correctamente")"""

    

    
    
