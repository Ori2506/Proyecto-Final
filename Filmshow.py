
from API import API
from Film import Film


class App:
    film_obj=[]

    def start(self):
        api = API()
        api.cargar_personajes()
        
        print("Starting the app...")


    def crear_films(self):
        db_films = self.cargar_api("https://www.swapi.tech/api/films/")
        for film in db_films:
                self.film_obj.append(Film(film["title"]),(film["episode_id"]),(film["release_date"]),(film["opening_crawl"]),(film["director"]) )

