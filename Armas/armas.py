import json
import random
import funciones_auxiliares

#Este programa es para crear objetos de la clase arma a partir de un archivo.json



    

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

    def __str__(self):
        return self.nombre

    def seleccionar_arma():
        lista_dict_armas=funciones_auxiliares.cargar_archivo("lista_de_armas.json", "No existe el archivo", "El archivo está corrupto")
        lista_armas=[] #Aquí se ubican todas las armas una vez creadas como objetos
        for dict_arma in lista_dict_armas:
            nueva_arma=Arma.from_dict(dict_arma)
            lista_armas.append(nueva_arma)
        arma_escogida=funciones_auxiliares.crear_menu(lista_armas, "¿Qué arma escoge?")
        return arma_escogida
        

        

        
    
