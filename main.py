import sys
if(len(sys.argv)!=3):raise Exception("Non hai inserito tutti i parametri");

from gui import *

from handle import *;
from generate import *;
import base64
from csvHandle import *;
from parameters import outFile;
from parameters import inFile;



matrices = readMatricesFromCSV(inFile)
for i in matrices:
    printMatrix(i)

writeOnCsv(outFile,matrProd(matrices[0],matrices[1]))
#a= fixedRowAndColumnsMatrix(2,3);
#t = transposedMatrix(a)
#print("Matrix A")
#printMatrix(a)
#print("Transposed A")
#printMatrix(t)
#print("A x Transposed A")
#printMatrix(matrProd(a,t))
#print("Transposed A x A")
#printMatrix(matrProd(t,a))
#initWritingCSV(outFile)
#writeOnCsv(outFile,a)
#writeOnCsv(outFile,t)
#writeOnCsv(outFile,matrProd(a,t))
#writeOnCsv(outFile,matrProd(t,a))
