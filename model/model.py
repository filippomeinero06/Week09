from database.dao import Dao

class Model:

    def __init__(self):
        pass


    def get_statistiche(self, serate):
        return Dao.read_statistiche(serate)

    def get_programma_ottimo(self, serate):
        lista_film = Dao.read_statistiche(serate)
        # Qui dovrei determinare il programma ottimo usando serate e lista_film: uso una strategia ricorsiva

        if ...:
            pass
        else:
            pass

        # Restituisco il programma ottimo
