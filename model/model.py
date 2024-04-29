import copy
import time


class Model:
    def __init__(self):
        self.N_iterazioni = 0
        self.N_soluzioni = 0
        self._soluzioni = []

    def risolvi_quadrato(self, N):
        self._ricorsione([], set(range(1, N * N + 1)), N)

    def _ricorsione(self, parziale, rimanenti, N):
        self.N_iterazioni += 1
        # caso terminale
        if len(parziale) == N * N:
            print(parziale)
            #if self.is_soluzione(parziale, N) == True:
            self.N_soluzioni += 1
            self._soluzioni.append(copy.deepcopy(parziale))
        # caso ricorsivo
        else:
            for i in rimanenti:
                parziale.append(i)
                if self.is_soluzione_parziale(parziale, N):
                    nuovi_rimanenti = copy.deepcopy(rimanenti)
                    nuovi_rimanenti.remove(i)                   # posso mettere una cifra una sola volta
                    self._ricorsione(parziale, nuovi_rimanenti, N)
                parziale.pop()

    def is_soluzione(self, parziale, N):
        numero_magico = N * (N*N + 1) / 2
        # vincolo 1 righe
        for row in range(N):          # per ognuna delle N righe
            somma = 0
            sottolista = parziale[row * N:(row+1)*N]
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False
        # vincolo 2 colonne
        for col in range(N):
            somma = 0
            sottolista = parziale[0 * N + col : (N-1) * N + col + 1: N]             # scandire le matrici in forma vettoriale sulle colonne
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False
        # vincolo 3 diag 1
        somma = 0
        for riga_col in range(N):
            somma += parziale[riga_col * N + riga_col]
            if somma != numero_magico:
                return False
        # vincolo 4 diag 2
        somma = 0
        for riga_col in range(N):
            somma += parziale[riga_col * N + (N - 1 - riga_col)]
            if somma != numero_magico:
                return False
        # tutti i vincoli soddisfatti
        return True


    def is_soluzione_parziale(self, parziale, N):
        numero_magico = N * (N * N + 1) / 2
        # vincolo 1 righe
        n_righe = len(parziale) // N
        for row in range(n_righe):  # per ognuna delle N righe
            somma = 0.0
            sottolista = parziale[row*N:(row+1)*N]
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False
        # vincolo 2 colonne
        n_col = max(len(parziale) - N*(N-1), 0)
        for col in range(n_col):
            somma = 0.0
            sottolista = parziale[0 * N + col : (N - 1) * N + col + 1: N]  # scandire le matrici in forma vettoriale sulle colonne
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False
        # vincolo 3 diag 1
        if len(parziale) == N*N:
            somma = 0.0
            for riga_col in range(N):
                somma += parziale[riga_col * N + riga_col]
            if somma != numero_magico:
                return False
        # vincolo 4 diag 2
        if len(parziale) == N*(N-1) +1:
            somma = 0.0
            for riga_col in range(N):
                somma += parziale[riga_col * N + (N - 1 - riga_col)]
            if somma != numero_magico:
                return False
        # tutti i vincoli soddisfatti
        return True

    def stampa_soluzione(self, soluzione, N):
        print("----------")
        for row in range(N):
            print([v for v in soluzione[row * N:(row + 1) * N]])
        print("----------")


if __name__ == "__main__":
    mdl = Model()
    start = time.time()
    N = 3
    mdl.risolvi_quadrato(N)
    end = time.time()
    for sol in mdl._soluzioni:
        mdl.stampa_soluzione(sol, N)
    print(f"Quadrato di lato {N}")
    print(f"{mdl.N_iterazioni} iterazioni")
    print(f"{mdl.N_soluzioni} soluzioni")
    print(f"{end - start} secondi")

    """
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for c in range(3):
        col = l[c: : 3]
        print(col)
    """