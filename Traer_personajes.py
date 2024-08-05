from API import API
from Personaje import Personaje
from PersonajeAPI import cargar_api
from PersonajeAPI import cargar_personajes
class Buscar_personaje:

    personajes_obj=[]
    def start_buscar_personaje(self):
        self.cargar_personaje()
        self.crear_personaje
        self.mostrar_personajes
    start_buscar_personaje()

    def crear_personaje(self):
        self.cargar_personajes()
        resultado_personaje=db_personajes["results"]
        for personaje in resultado_personaje:
            self.personajes_obj.append(Personaje(nombre=personaje["results"]["properties"]["name"],planeta_origen=personaje["results"]["properties"]["homeworld"], genero=personaje["results"]["properties"]["gender"]))
    
    def mostrar_personajes(self):
        personaje:Personaje
        for personaje in self.personajes_obj:
            print(f"Nombre: {self.nombre}")
            print(f"Planeta de origen:  {self.planeta_origen}")
            print(f"Genero: {self.genero}")
            print("----")

                                       