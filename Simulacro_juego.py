
import funciones_auxiliares
import modulo_armas
import random
import clases
import armaduras
import creacion_personaje
#-------------------------------------------------------------------------------------

lista_personajes=funciones_auxiliares.cargar_archivo("archivo_personajes.json", "el archivo no existe", "El archivo está dañado")
mi_personaje=funciones_auxiliares.crear_menu_por_nombre(lista_personajes, "Nombre", "Elige el personaje: ")
personaje=creacion_personaje.Personaje.from_dict(mi_personaje)
lista_personajes=funciones_auxiliares.cargar_archivo("archivo_personajes.json", "el archivo no existe", "El archivo está dañado")
mi_personaje=funciones_auxiliares.crear_menu_por_nombre(lista_personajes, "Nombre", "Elige el enemigo: ")
enemigo=creacion_personaje.Personaje.from_dict(mi_personaje)

print (personaje, personaje.puntos_de_golpe)
print (enemigo, enemigo.puntos_de_golpe)
turno=1

while personaje.puntos_de_golpe>0 and enemigo.puntos_de_golpe>0:
    print (f"---------------Asalto {turno}------------")
    personaje.atacar(enemigo)
    print (enemigo, enemigo.puntos_de_golpe)
    enemigo.atacar(personaje)
    print (personaje, personaje.puntos_de_golpe)
    turno+=1
    

print (personaje, personaje.puntos_de_golpe)
print (enemigo, enemigo.puntos_de_golpe)



    
personaje=creacion_personaje.Personaje.from_dict(mi_personaje)
print (personaje)
print (personaje.armadura_equipada)
print(personaje.clase_de_armadura)
print (personaje.armadura_equipada.resistencias)
personaje.equipar_armadura()
print (personaje.armadura_equipada)
print(personaje.clase_de_armadura)
print (personaje.armadura_equipada.resistencias)
personaje.desequipar_armadura()
print (personaje.armadura_equipada)
print(personaje.clase_de_armadura)

