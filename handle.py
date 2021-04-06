import numpy as np
from parameters import valueBound
from math import cos, sin, radians

# stampa matrice e precedentemente il numero di righe  e colonne
def toStringMatrix(m):  
    tmpBound = valueBound
    printDims(m)
    string = ""
    maxChar = len(str(tmpBound)) +1 
    minDigit = len(str(minMaxMatr(m)[0]))+1
    maxDigit = len(str(minMaxMatr(m)[1]))+1
    if(maxChar<minDigit or maxChar < maxDigit):
        if(minDigit>=maxDigit):
            maxChar = minDigit;
        else:
            maxChar = maxDigit;
    for row in range(len(m)):
        for col in range(len(m[row])):
            digits = len(str(m[row][col]))    
            for i in range(maxChar-digits):
                string+=" "     
            string+=str(m[row][col])
        string+="\n"  
    return string
    


def minMaxMatr(m):
    dup = []
    for k in m:
        for i in k:
            dup.append(i)
    return [min(dup), max(dup)]




# somma di matrici
def addMatrix(a, b):
    dimsA = dims(a)
    dimsB = dims(b)
    if(dimsA[0] != dimsB[0] or dimsA[1] != dimsB[1]):
        raise Exception(
            "C'è un diverso numero di righe o colonne, non posso fare la somma")
    C = []
    r = 0
    while(r < len(a)):
        c = 0
        C.append([])
        while(c < len(a[r])):
            C[r].append(a[r][c]+b[r][c])
            c += 1
        r += 1
    return C

# numero righe e numero colonne di una matrice


def dims(a):
    return [len(a), len(a[0])]

# stampa numero righe e numero colonne di una matrice


def printDims(a):
    d = dims(a)
    print("Rows: "+str(d[0]))
    print("Columns: "+str(d[1]))

def printMatrix(m):
    print(toStringMatrix(m))


# prodotto tra matrici
def matrProd(a, b):
    dimsA = dims(a)
    dimsB = dims(b)
    if(dimsA[1] != dimsB[0]):
        raise Exception(
            "La prima matrice deve avere un numero di colonne pari al numero di righe della seconda matrice")
    X = []
    r = 0
    while(r < dimsA[0]):
        X.append([])
        c = 0
        while(c < dimsB[1]):
            #X[r]=X[r] + ris(a[r],getColumn(b,c));
            X[r].append((int)(ris(a[r], getColumn(b, c))))
            c += 1
        r += 1
    return X

# restituisce una colonna


def getColumn(z, col):
    v = []
    i = 0
    while(i < len(z)):
        v.append(z[i][col])
        i += 1
    return v

# funzione ausiliara che restituisce il risultato di riga x colonna


def ris(x, y):
    sum = 0
    i = 0
    while(i < len(x)):
        sum += x[i]*y[i]
        i += 1
    return sum

# dice se la matrice è quadrata


def isQuadrata(m):
    return dims(m)[0] == dims(m)[1]

# crea l'elemento neutro della somma, cioè la matrice vuota

def makeEmptyMatrix(r, c):
    X = []
    for row in range(r):
        X.append([])
        for column in range(c):
            X[row].append(0);
    return X


# crea l'elemento neutro della somma, cioè la matrice vuota (quadrata)


def makeEmptySquareMatrix(n):
    X = []
    for row in range(n):
        X.append([])
        for column in range(n):
            X[row].append(0);
    return X

# riempie la diagonale di una matrice


def getFullfilledDiagonal(m, _lambda_):
    lenght = dims(m)[0]
    X = m
    i = 0
    while(i < lenght):
        X[i][i] = _lambda_
        i += 1
    return X

# crea l'elemento neutro del prodotto, cioè la matrice identica


def getIdentica(m):
    if (not isQuadrata(m)):
        raise Exception("Deve essere quadrata")
    lenght = dims(m)[0]
    X = makeEmptySquareMatrix(lenght)
    return getFullfilledDiagonal(X, 1)

# permette di moltiplicare per una matrice scalare

def getScalare(m, _lambda_):
    if (not isQuadrata(m)):
        raise Exception("Deve essere quadrata")
    lenght = dims(m)[0]
    X = makeEmptySquareMatrix(lenght)
    X = getFullfilledDiagonal(X, _lambda_)
    return matrProd(m, X)

def rotate2x2Matrix90Degrees(m):
    if ((not isQuadrata(m))and len(m)!=2):
        raise Exception("Input sbagliato")  
    thetaRad = radians(90)
    R=[[cos(thetaRad),-sin(thetaRad)],
       [sin(thetaRad),cos(thetaRad)]]
    return matrProd(R,m)

def transposedMatrix(m):
    mDims = dims(m)
    tRows = mDims[1]
    tCols = mDims[0]
    T = []
    for r in range(tRows):
        T.append([])
        for c in range(tCols):
            T[r].append(m[c][r])

    return T

