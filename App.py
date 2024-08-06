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

    def crear_mision(self):
        print("")
        # print("Creemos una nueva misión")
        # nombre_mision=input("Ingrese el nombre de la mision: ")
        # while True:
        #     planeta_destino = input("Ingrese el planeta destino: ")
        #     if planeta_destino not in #lista de planetas objetos
        #         print("Planeta inválido")
        #     else:
        #         break

        # armas_utilizar = []
        # n = 0

        # while n < 7:
        #     arma_seleccionada = input("Ingrese una arma o 0 para finalizar: ")

        #     if arma_seleccionada==0:
        #         break
        #     elif arma_seleccionada in #lista de armas
        #         armas_utilizar.append(arma_seleccionada)
        #         n += 1
        #     else:
        #         print("Arma inválida. Intente nuevamente.")

        #     integrantes_mision=[]
        #     m=0

        # while n<7:
        #     integrante_seleccionado= input("Ingrese un integrante de la misión o 0 para finalizar: ")

        #     if integrante_seleccionado==0:
        #         break
        #     elif integrante_seleccionado in #lista de people
        #         integrantes_mision.append(integrante_seleccionado)
        #         m+=1
        #     else:
        #         print("Integrante inválido. Intente nuevamente")

        




#para probar
def main():
    app=App()
    app.start()

main()