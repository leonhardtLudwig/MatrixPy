from random import randint
from handle import makeEmptyMatrix
from parameters import rowBound
from parameters import columnBound
from parameters import valueBound

def setRowBound(b):
    if(b<0):
        raise Exception("Non possono esserci valori negativi per le righe") 
    rowBound = b

def setColumnBound(b):
    if(b<0):
        raise Exception("Non possono esserci valori negativi per le colonne") 
    columnBound = b

def setValueBound(b):
    print("Attenzione, il limite di valori inserito è intorno allo 0")
    if(b<0):
        valueBound = -b
    else:
        valueBound = b

def ranValue():
    return int(pow(-1,randint(-valueBound,valueBound)))*randint(-valueBound,valueBound)

def ranCol():
    return randint(1,columnBound)

def ranRow():
    return randint(1,rowBound)

#ran row rand col
def randomMatrix():
    c = ranCol()
    r = ranRow()
    M = makeEmptyMatrix(r,c)
    for row in range(r):
        for column in range(c):
            M[row][column]=ranValue()
    return M

#fix row rand col
def fixedRowsMatrix(rows):
    c = ranCol()
    r = rows
    M = makeEmptyMatrix(r,c)
    for row in range(r):
        for column in range(c):
            M[row][column]=ranValue()
    return M


#rand row fix col
def fixedColumnsMatrix(columns):
    c = columns
    r = ranRow()
    M = makeEmptyMatrix(r,c)
    for row in range(r):
        for column in range(c):
            M[row][column]=ranValue()
    return M


#fix row fix col
def fixedRowAndColumnsMatrix(row, columns):
    c = columns
    r = row
    M = makeEmptyMatrix(r,c)
    for row in range(r):
        for column in range(c):
            M[row][column]=ranValue()
    return M

#rand square
def randomSquareMatrix():
    c = ranCol()
    r = c
    M = makeEmptyMatrix(r,c)
    for row in range(r):
        for column in range(c):
            M[row][column]=ranValue()
    return M

#rand fixed square
def randomFixedSquareMatrix(n):
    c = n
    r = n
    M = makeEmptyMatrix(r,c)
    for row in range(r):
        for column in range(c):
            M[row][column]=ranValue()
    return M
