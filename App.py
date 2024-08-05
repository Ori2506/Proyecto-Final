from ApiFilm import cargar_api
from API import API
from Film import Film
class App:
    film_obj=[]

    def start(self):
        self.crear_films()
        self.print_films()
        api = API()
        api.cargar_personajes()
        
        print("Starting the app...")

    def crear_films(self):
        db_films=cargar_api("https://www.swapi.tech/api/films/")
        key_films=db_films["result"]
        for film in key_films:
            self.film_obj.append(Film(title=film['properties']["title"],episode_id=film['properties']["episode_id"],release_date=film['properties']["release_date"],opening_crawl=film['properties']["opening_crawl"],director=film['properties']["director"]))
  
    def print_films(self):
        for film in self.film_obj:
            print(f"Titulo: {film.title}")
            print(f"Numero de episodio: {film.episode_id}")
            print(f"Fecha de lanzamiento: {film.release_date}")
            print(f"Opening Crawl: {film.opening_crawl}")
            print(f"Director: {film.director}")
            print("---")

def main():
    app=App()
    app.start()

main()