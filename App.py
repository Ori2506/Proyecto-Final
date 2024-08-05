
from API import API


class App:
    film_obj=[]

    def start(self):
        api = API()
        api.cargar_personajes()
        
        print("Starting the app...")