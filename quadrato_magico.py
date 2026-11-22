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

        # CORRETTO: le righe già complete hanno n colonne, non num_colonne_sol
        for r in range(0, num_righe_sol):
            somma = 0
            for c in range(0, n):
                somma += sol_parziale[r*n + c]
            if somma != M:
                return False

        # Idem per colonne e diagonali

        # Somme delle colonne
        # CORRETTO: controllo tutte le colonne, non solo le prime num_colonne_sol.
        # Una colonna ha una cella in più se è già stata toccata dalla riga in corso.
        for c in range(0, n):
            if c < num_colonne_sol:
                righe_colonna = num_righe_sol + 1
            else:
                righe_colonna = num_righe_sol
            somma = 0
            for r in range(0, righe_colonna):
                somma += sol_parziale[r*n + c]
            if righe_colonna == n:      # colonna completa: deve fare esattamente M
                if somma != M:
                    return False
            elif somma >= M:            # colonna incompleta: mancano numeri positivi, deve restare < M
                return False

        # Somma delle diagonali
        # CORRETTO: le diagonali si controllano solo a quadrato completo
        if len(sol_parziale) == n*n:
            somma = 0
            for r in range(0, n):
                somma += sol_parziale[r*n + r]
            if somma != M:
                return False

            somma = 0
            for r in range(0, n):
                somma += sol_parziale[r*n + (n-1-r)]
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
                sol_parziale.pop() # CORRETTO: fuori dall'if, perché l'append lo faccio sempre


if __name__ == '__main__':
    qm = QuadratoMagico()
    soluzioni = qm.risolvi(3)
    print(soluzioni)
    print(qm._num_soluzioni)