from database.dao import Dao

class Model:

    def __init__(self):
        self._miglior_programma = []
        self._miglior_punteggio = -1


    def get_statistiche(self, serate):
        return Dao.read_statistiche(serate)

    def get_programma_ottimo(self, serate):
        lista_film_serate = Dao.read_film_serata(serate)
        '''for f in lista_film_serate:
            print(f)'''
        # Qui dovrei determinare il programma ottimo usando serate e lista_film_serate: uso una strategia ricorsiva

        # Così ogni volta che chiamo la funzione riparto da capo (non sovrascrivo i dati)
        self._miglior_programma = []
        self._miglior_punteggio = -1

        # []: soluzione parziale che appende
        # lista_film_serate: lista dove prende i dati che gli servono
        # serate: è il vincolo di num di serate (6, 9 o 12)
        self._ricorsione([], lista_film_serate, serate)

        if self._miglior_punteggio == -1:
            return [], 0

        return self._miglior_programma, self._miglior_punteggio

    def _ricorsione(self, parziale, lista_film_serate, serate):
        # Condizione di terminazione
        if len(parziale) == serate:
            punteggio = self._calcola_punteggio(parziale)

            if punteggio > self._miglior_punteggio:
                self._miglior_punteggio = punteggio
                self._miglior_programma = parziale.copy()   # ATTENZIONE: fare sempre la COPIA!
            return

        serata = len(parziale) + 1

        # Quattro film per ogni serata
        for film in lista_film_serate[(serata - 1)*4 : serata*4]:
            if self._vincoli_soddisfatti(parziale, film, serate):
                parziale.append(film)
                self._ricorsione(parziale, lista_film_serate, serate)
                parziale.pop()  # Backtracking


    def _vincoli_soddisfatti(self, parziale, film, serate):
        # 1) Due film consecutivi non possono avere lo stesso genere
        if len(parziale) > 0:
            if parziale[-1].genere == film.genere:
                return False

        # 2) Un genere non può comparire più di due volte
        occorrenze = 0
        for scelto in parziale:
            if scelto.genere == film.genere:
                occorrenze += 1

        if occorrenze > 2:
            return False

        # 3) Vincoli che si possono fare alla fine di tutto
        if len(parziale) + 1 == serate:     # Se il num di film già scelti  +  il film che sto per aggiungere è uguale al num di serate, allora ho campletato il programma
            num_commedie = 0
            generi_diversi = set()

            # Qui controllo i film che ho già scelto nella soluzione parziale
            for scelto in parziale:
                if scelto.genere == "Comedy":
                    num_commedie += 1
                generi_diversi.add(scelto.genere)

            # Qui controllo ancora il film che voglio aggiungere
            if film.genere == "Comedy":
                num_commedie += 1
            generi_diversi.add(film.genere)

            if num_commedie < 2 or len(generi_diversi) < 3:
                return False
        return True

    def _calcola_punteggio(self, programma):
        punteggio = 0
        for film in programma:
            punteggio += film.media
        return punteggio