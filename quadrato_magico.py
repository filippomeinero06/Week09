import copy


class QuadratoMagico:
    def __init__(self):
        self._soluzioni = []
        self._num_soluzioni = 0

    def _genera_rimanenti(self, n):
        rimanenti = []
        for i in range(1, n*n + 1): # Se n = 3, 3*3+1 quindi da 1 a 9
            rimanenti.append(i)
        return rimanenti

    def _stampa_soluzione(self, soluzione, n):
        print("-------")
        for r in range(0, n):
            for c in range(0, n):
                print(soluzione[r*n + c], end=" ")
            print()
        print("-------")


    def risolvi(self, n):
        self._ricorsione([], self._genera_rimanenti(n), n)
        return self._soluzioni

    def _soluzione_sta_venendo_bene(self, sol_parziale, n):
        M = (n * (n * n + 1)) / 2
        # Se non è vero che tutti gli elementi delle righe sommano a M --> return False

        # Somme delle righe
        num_righe_sol = len(sol_parziale) // n
        num_colonne_sol = len(sol_parziale) - n*num_righe_sol

        for r in range(0, num_righe_sol):
            somma = 0
            for c in range(0, num_colonne_sol):
                somma += sol_parziale[r*n + c]
            if somma != M:
                return False

        # Idem per colonne e diagonali

        # Somme delle colonne
        for c in range(0, num_colonne_sol):
            somma = 0
            for r in range(0, num_righe_sol):
                somma += sol_parziale[r*n + c]
            if somma != M:
                return False

        # Somma delle diagonali
        somma = 0
        for r in range(0, num_righe_sol):
            for c in range(0, num_colonne_sol):
                somma += sol_parziale[r*n + c]
            if somma != M:
                return False

        somma = 0
        for r in range(num_righe_sol, -1, -1):
            for c in range(num_colonne_sol, -1, -1):
                somma += sol_parziale[r * n + c]
            if somma != M:
                return False

        # Se sta venendo bene
        return True

    def _ricorsione(self, sol_parziale, rimanenti, n):
        if len(sol_parziale) == n*n:    # Se abbiamo messo tutti i numeri nella soluzione
            self._soluzioni.append(copy.deepcopy(sol_parziale)) # Sempre fare la COPIA PROFONDA
            self._num_soluzioni += 1
            #self._stampa_soluzione(sol_parziale, n)


        else:
            # Soluzione non ottimizzata
            """   
            for i in rimanenti:             
                sol_parziale.append(i)
                nuovi_rimanenti = copy.deepcopy(rimanenti)  # Attenzione alle liste
                nuovi_rimanenti.remove(i)
                self._ricorsione(sol_parziale, nuovi_rimanenti, n)
                sol_parziale.pop()
            """

            # Per ottimizzare, posso chiedermi se la soluzione che sto andando a generare, possa
            # alla fine essere valida, oppure se posso già abortire perché i vincoli non rispettati

            # Soluzione ottimizzata
            for i in rimanenti:
                sol_parziale.append(i) # Sulla sol. parziale non utilizzare deepcopy nella ricorsione
                if self._soluzione_sta_venendo_bene(sol_parziale, n):
                    nuovi_rimanenti = copy.deepcopy(rimanenti)  # Attenzione alle liste, deepcopy perché è un'informazione nuova per il livello successivo
                    nuovi_rimanenti.remove(i)
                    self._ricorsione(sol_parziale, nuovi_rimanenti, n)
                    sol_parziale.pop()







if __name__ == '__main__':
    qm = QuadratoMagico()
    soluzioni = qm.risolvi(4)
    #print(soluzioni)
    print(qm._num_soluzioni)