import csv

def initWritingCSV(fileName):
    with open(fileName, 'w', newline='') as file:  
        writer = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC, delimiter=';')


def writeOnCsv(fileName, matrix):
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file,quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
        writer.writerows(matrix)
        writer.writerow([])


def readMatricesFromCSV(fileName):
    matrs = [[]]
    nMatr = 0
    with open(fileName) as file:
        reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
        for row in reader: 
            if(row==[]):
                matrs.append([])
                nMatr+=1
            else:
                matrs[nMatr].append(row)
    if(matrs[len(matrs)-1]==[]):matrs.pop()
    return matrs
