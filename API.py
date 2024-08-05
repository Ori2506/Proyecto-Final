import requests as rq

class API:

    def cargar_api(self, link):
        response = rq.get(link)
        print(response.json())
        return response.json()

    def cargar_personajes(self):
        personajes = self.cargar_api('https://www.swapi.tech/api/people')
        return personajes

    def cargar_films(self):
        db_films = self.cargar_api("https://www.swapi.tech/api/films/")
        return db_films
    
    def cargar_planet(self):
        db_planets =self.cargar_api("https://www.swapi.tech/api/planets/")
        return db_planets
    
    def cargar_species(self):
        db_species=self.cargar_api("https://www.swapi.tech/api/species/")
        return db_species
    
    def cargar_starships(self):
        db_starships=self.cargar_api("https://www.swapi.tech/api/starships/")
        return db_starships
    
    def cargar_vehicles(self):
        db_vehicles=self.cargar_api("https://www.swapi.tech/api/vehicles/")
        return db_vehicles

