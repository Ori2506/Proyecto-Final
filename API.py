import requests as rq
from Especie import Especie
from Planeta import Planeta

class API:

    def cargar_api(self, link):
        response = rq.get(link)        
        return response.json()

    # metodo para cargar los personajes
    def cargar_personajes(self):
        personajes = self.cargar_api('https://www.swapi.tech/api/people')
        return personajes

