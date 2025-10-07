import funciones_auxiliares
import modulo_armas
import random
import clases
import armaduras

#-----------------------Funciones propias para la creación de persoanjes----------------

def crear_personaje():
    nombre=input("Escriba el nombre del personaje")
    raza=funciones_auxiliares.crear_menu(["Humano", "Elfo", "Semielfo", "Enano", "Mediano", "Gnomo"], "Escoja la raza")
    clase=clases.escoger_clase_DND().to_dict()
    print ("A continuación puntuará la habilidades. Los valores irán de 3 a 18 puntos")
    diccionario_puntuacion_caracteristicas=puntuar_caracteristicas()
    diccionario_bonificadores_caracteristicas=bonificaciones_caracteristicas(diccionario_puntuacion_caracteristicas)
    arma_equipada=equipar_arma()
    armadura_equipada=armaduras.seleccionar_armadura()
    return{"Nombre":nombre, "Raza":raza, "Clase":clase, "Puntuación de las caracterisicas": diccionario_puntuacion_caracteristicas,
           "Bonificacion por caracteristicas":diccionario_bonificadores_caracteristicas, "Arma equipada": arma_equipada, "Armadura equipada":armadura_equipada}



def puntuar_caracteristicas():
    tupla_caracteristicas= ("Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma")
    valores_caracteristicas={}
    for caracteristica_individual in tupla_caracteristicas:
        valores_caracteristicas[caracteristica_individual]=funciones_auxiliares.solicitar_entero(3, 18, f"¿Cuál es el valor de {caracteristica_individual}?")
    return valores_caracteristicas


def bonificaciones_caracteristicas(diccionario_puntuacion_caracteristicas):
    dict_bonificaciones_caracteristicas={}
    for caracteristica_individual in diccionario_puntuacion_caracteristicas:
            dict_bonificaciones_caracteristicas[caracteristica_individual]=diccionario_puntuacion_caracteristicas[caracteristica_individual]//2-5
    return dict_bonificaciones_caracteristicas

def añadir_personaje_a_archivo(): #Añade diccionario con caraterísticas de un arma a la lista de armas, que se guarda en un archivo .json 
    nuevo_personaje=crear_personaje()
    lista_actualizada=funciones_auxiliares.cargar_archivo ("archivo_personajes.json", "Se ha creado un archivo nuevo", "El archivo está corrupto")
    lista_actualizada.append(nuevo_personaje)
    funciones_auxiliares.guardar_en_archivo("archivo_personajes.json", lista_actualizada)
    print ("El personaje se ha añadido correctamente")

def equipar_arma():
    arma_equipada=modulo_armas.seleccionar_arma()
    return arma_equipada



#---------------------Clase personaje----------------------------
class Personaje:
    def __init__(self, diccionario_caracteristicas):
        self.nombre=diccionario_caracteristicas["Nombre"]
        self.raza=diccionario_caracteristicas["Raza"]
        self.clase=clases.ClaseBase.from_dict(diccionario_caracteristicas["Clase"])
        self.puntuacion_caracteristicas=diccionario_caracteristicas["Puntuación de las caracterisicas"]
        self.bonificacion_caracteristicas=diccionario_caracteristicas["Bonificacion por caracteristicas"]
        self.arma_equipada=modulo_armas.Arma.from_dict(diccionario_caracteristicas["Arma equipada"])
        self._armadura_equipada=armaduras.ArmaduraBase.from_dict(diccionario_caracteristicas["Armadura equipada"])
        self.puntos_de_golpe=self.bonificacion_caracteristicas["Constitución"]+self.clase.dado_de_golpe
        #self.clase_de_armadura=10+self.armadura_equipada.clase_armadura+self.bonificacion_caracteristicas["Destreza"]#+self.clase.bonificar_clase_armadura(self.bonificacion_caracteristicas, self.armadura_equipada)

    @property
    def armadura_equipada(self):
            return self._armadura_equipada



    @property
    def clase_de_armadura(self):
            return 10+self._armadura_equipada.calcular_CA_base(self.bonificacion_caracteristicas["Destreza"])+self.clase.bonificador_clase_armadura(self.bonificacion_caracteristicas, self._armadura_equipada)

    def __str__(self):
        return self.nombre

    @classmethod
    def from_dict(cls, diccionario_caracteristicas):
        return cls (diccionario_caracteristicas)

    def atacar(self, enemigo):
        if self.puntos_de_golpe>0:
            print (f"Turno de {self.nombre}")
            ataque=self.arma_equipada.bonificador_ataque(self)+random.randint(1,20)
            print (f"Ataque de {self.nombre}: {ataque}({self.arma_equipada.bonificador_ataque(self)}) -- Clase armadura de {enemigo} {enemigo.clase_de_armadura}")
            if ataque>=enemigo.clase_de_armadura:
                daño=self.arma_equipada.calcular_daño()
                print (f"{self.nombre} ha consguido golpear a {enemigo.nombre}. Le ha hecho {daño} puntos de golpe")
                enemigo.puntos_de_golpe-=daño
            else:
                print("No has conseguido golpear a tu enemigo")
        else:
            pass


    def equipar_arma(self, nueva_arma):
        self.arma_equipada=modulo_armas.Arma.from_dict(nueva_arma)

    def equipar_armadura(self):
        nueva_armadura=armaduras.seleccionar_armadura()
        self._armadura_equipada=armaduras.ArmaduraBase.from_dict(nueva_armadura)
        
    def desequipar_armadura(self):
        self._armadura_equipada=armaduras.SinArmadura()
        

    
       


                                                  

#------------------------------bloque principal--------------------------


        

if __name__=="__main__":

    añadir_personaje_a_archivo()
    
    
 
   


    
