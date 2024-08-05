class Personaje:
    personajes_obj=[]
    def __init__(self, nombre, planeta_origen,genero):
        self.nombre = nombre
        self.planeta_origen = planeta_origen
        self.episodios=0
        self.genero=genero
        self.especie=0
        self.naves=0
        self.vehiculos=0