import funciones_auxiliares
import modulo_armas
import random
import clases

#-----------------------Funciones propias para la creación de persoanjes----------------

def crear_personaje():
    nombre=input("Escriba el nombre del personaje")
    raza=funciones_auxiliares.crear_menu(["Humano", "Elfo", "Semielfo", "Enano", "Mediano", "Gnomo"], "Escoja la raza")
    clase=clases.escoger_clase_DND().to_dict()
    print ("A continuación puntuará la habilidades. Los valores irán de 3 a 18 puntos")
    diccionario_puntuacion_caracteristicas=puntuar_caracteristicas()
    diccionario_bonificadores_caracteristicas=bonificaciones_caracteristicas(diccionario_puntuacion_caracteristicas)
    arma_equipada=equipar_arma()
    return{"Nombre":nombre, "Raza":raza, "Clase":clase, "Puntuación de las caracterisicas": diccionario_puntuacion_caracteristicas, "Bonificacion por caracteristicas":diccionario_bonificadores_caracteristicas, "Arma equipada": arma_equipada}




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
        self.puntos_de_golpe=self.bonificacion_caracteristicas["Constitución"]+self.clase.dado_de_golpe

    def __str__(self):
        return self.nombre

    @classmethod
    def from_dict(cls, diccionario_caracteristicas):
        return cls (diccionario_caracteristicas)

    def atacar(self, enemigo):
        ataque=self.bonificacion_caracteristicas["Fuerza"]+random.randint(1,20)
        if ataque>=enemigo.bonificacion_caracteristicas["Destreza"]+10:
    
            daño=self.arma_equipada.calcular_daño()
            print (f"{self.nombre} ha consguido golpear a {enemigo.nombre}. Le ha hecho {daño} puntos de golpe")
        else:
            print("No has conseguido golpear a tu enemigo")


    def equipar_arma(self, nueva_arma):
        
        self.arma_equipada=modulo_armas.Arma.from_dict(nueva_arma)
        

    
       


                                                  

#------------------------------bloque principal--------------------------


        

if __name__=="__main__":

   # añadir_personaje_a_archivo()
    
    lista_personajes=funciones_auxiliares.cargar_archivo("archivo_personajes.json", "el archivo no existe", "El archivo está dañado")
    mi_personaje=funciones_auxiliares.crear_menu_por_nombre(lista_personajes, "Nombre", "Elige el personaje")
    personaje=Personaje.from_dict(mi_personaje)
    print (f"{personaje} lleva equipada {personaje.arma_equipada}")
    print (f"{personaje} tiene { personaje.puntos_de_golpe} puntos de golpe")
    print (personaje.arma_equipada.calcular_daño())
    print (f"La clase de {personaje} es {personaje.clase}")

    """ lista_personajes=funciones_auxiliares.cargar_archivo("archivo_personajes.json", "el archivo no existe", "El archivo está dañado")
    mi_enemigo=funciones_auxiliares.crear_menu_por_nombre(lista_personajes, "Nombre", "Elige el enemigo")
    enemigo=Personaje.from_dict(mi_enemigo)
    print (f"{enemigo} lleva equipada {enemigo.arma_equipada}")
    print (personaje.arma_equipada.calcular_daño())"""

    #print(f"{personaje} encuentra la espada divina. Un arma legendaria que es capaz de detectar el mal. Nuestro héroe decide guardar su daga para equiparse con la nueva arma")
    #espada_divina={"Nombre": "Espada_divina", "Daño":{"Cortante":100, "Divino":500}, "Peso":2}
    #personaje.equipar_arma(espada_divina)
    #print (f"{personaje} lleva equipada {personaje.arma_equipada}")
    #print (personaje.arma_equipada.calcular_daño())

    #personaje.atacar(enemigo)
 

   


    
