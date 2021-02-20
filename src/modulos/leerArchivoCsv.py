import csv

with open('src/modulos/ejemplo.csv', newline='') as csvfile:
    miCsv = csv.reader(csvfile, delimiter= ',', quotechar = '|')
    for linea in miCsv:
        print('-'.join(linea))