from math import *

def loese_lgs(A, b):
    n = len(b)
    
    # Gauß-Elimination
    for i in range(n):
        # Pivotisierung (nur wenn nötig)
        if A[i][i] == 0:
            for k in range(i+1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    b[i], b[k] = b[k], b[i]
                    break
        
        pivot = A[i][i]
        if pivot == 0:
            raise ValueError("Kein eindeutiges LGS (Pivot bleibt 0)")
        
        # Normieren
        for j in range(i, n):
            A[i][j] = A[i][j] / pivot
        b[i] = b[i] / pivot
        
        # Eliminieren
        for k in range(n):
            if k != i:
                faktor = A[k][i]
                for j in range(i, n):
                    A[k][j] -= faktor * A[i][j]
                b[k] -= faktor * b[i]
    
    return b


def polynom_bestimmen(punkte):
    n = len(punkte)
    grad = n - 1
    
    # Matrix A und Vektor b aufstellen
    A = []
    b = []
    
    for (x, y) in punkte:
        zeile = []
        for i in range(grad, -1, -1):
            zeile.append(x ** i)
        A.append(zeile)
        b.append(y)
    
    koeff = loese_lgs(A, b)
    
    return koeff, grad


def ausgabe(koeff, grad):
    print("Grad des Polynoms/max. Anzahl Nullstellen:", grad)
    print("Polynom:")
    
    s = "y = "
    n = len(koeff)
    
    for i in range(n):
        a = koeff[i]
        pot = grad - i
        
        if i > 0 and a >= 0:
            s += "+"
        
        if pot > 1:
            s += str(round(a, 5)) + "*x^" + str(pot)
        elif pot == 1:
            s += str(round(a, 5)) + "*x"
        else:
            s += str(round(a, 5))
    
    print(s)


def main():
    punkte = []
    n = int(input("Anzahl Punkte: "))
    
    for i in range(n):
        x = float(input("x" + str(i+1) + ": "))
        y = float(input("y" + str(i+1) + ": "))
        punkte.append((x, y))
    
    koeff, grad = polynom_bestimmen(punkte)
    ausgabe(koeff, grad)


main()
