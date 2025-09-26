#----------------Se crea la clase armadura--------------
class ArmaduraBase:
    def __init__ (self, armadura_dict):
        self.nombre=armadura_dict["Nombre_armadura"]
        self.clase_armadura=armadura_dict["valor_clase_armadura"]

    def Calcular_CA_base (self, destreza_del_personaje):
        """
    Método que las subclases sobrescribirán para su lógica de bonificador.
    """
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

    def __str__(self):
        return self.nombre

class ArmaduraLigera(ArmaduraBase):
    def __init__ (self, armadura_dict):
        super().__init__(armadura_dict)  #Se lo pasa a la clase padre como atributo

    def calcular_CA_base (self, destreza_del_personaje):
        return destreza_del_personaje+self.clase_armadura

class ArmaduraIntermedia (ArmaduraBase):
    def __init__ (self, armadura_dict, limite_bonificador_destreza):
        super().__init__(armadura_dict)
        self.limite_bonificador_destreza=limite_bonificador_destreza

    def calcular_CA_base (self, destreza_del_personaje):
        return min(destreza_del_personaje, self.limite_bonificador_destreza)+self.clase_armadura

class ArmaduraPesada (ArmaduraBase):
    def __init__ (self, armadura_dict):
        super().__init__(armadura_dict)

    def calcular_CA_base (self, destreza_del_personaje):
        return self.clase_armadura

    





#---------------Se crean los objetos armadura-------------      

coraza=ArmaduraIntermedia({"Nombre_armadura": "Coraza", "valor_clase_armadura":14}, 2)
cota_de_malla=ArmaduraPesada({"Nombre_armadura": "Cota de malla", "valor_clase_armadura": 16})
armadura_acolchada=ArmaduraLigera({"Nombre_armadura": "Armadura acolchada", "valor_clase_armadura": 11})
armadura_de_cuero=ArmaduraLigera({"Nombre_armadura": "Armadura de cuero", "valor_clase_armadura": 11})
armadura_de_cuero_tachonado=ArmaduraLigera({"Nombre_armadura": "Armadura de cuero tachonado", "valor_clase_armadura": 12})
sin_armadura=ArmaduraLigera ({"Nombre_armadura": "Sin armadura", "valor_clase_armadura": 10})                        


    #-----------Se crea un diccionario donde se guardan todos los objetos de tipo Armadura que vayan surgiendo a partir de los diccionario con los datos de armaduras-------
armaduras_del_juego={       
    coraza.nombre: coraza,
    cota_de_malla.nombre: cota_de_malla,
    armadura_acolchada.nombre:armadura_acolchada,
    armadura_de_cuero.nombre: armadura_de_cuero,
    armadura_de_cuero_tachonado.nombre: armadura_de_cuero_tachonado,
    sin_armadura.nombre:sin_armadura
    }#diccionario
lista_armaduras_del_juego=list(armaduras_del_juego.values())




